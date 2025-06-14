from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Tree, Input, Button, Label, Static
from textual.widgets.tree import TreeNode
from textual.containers import Container, Horizontal
from config import (
    load_platform_commands,
    load_user_commands,
    save_user_commands,
)
from clipboard_utils import copy_to_clipboard
import json
from pathlib import Path

FAV_PATH = Path("favorites.json")

def load_favorites():
    if FAV_PATH.exists():
        with open(FAV_PATH, "r") as f:
            return json.load(f)
    return []

def save_favorites(commands: list[dict]):
    with open(FAV_PATH, "w") as f:
        json.dump(commands, f, indent=2)

def is_fav(cmd, favorites):
    return any(
        fav.get("command") == cmd["command"] and fav.get("name") == cmd["name"]
        for fav in favorites
    )

class AddCommandDialog(Static):
    def compose(self) -> ComposeResult:
        yield Label("Add Custom Command", id="dialog-title")
        yield Input(placeholder="Name", id="cmd_name")
        yield Input(placeholder="Command", id="cmd_command")
        yield Input(placeholder="Description", id="cmd_desc")
        yield Horizontal(
            Button("Cancel", id="cancel"),
            Button("Add", id="add"),
            id="dialog-buttons"
        )

class CommandTree(Tree):
    def load_nodes(self, node: TreeNode, children: list[dict], custom_commands=None, favorites=None) -> None:
        if favorites is None:
            favorites = []

        # 1. Normale Struktur
        for entry in children:
            if "children" in entry:
                child = node.add(
                    entry["label"],
                    data={"type": "folder", "children": entry["children"]},
                )
                child.allow_expand = True
            else:
                node.add_leaf(
                    f"{entry['name']} – {entry['description']}",
                    data={"type": "command", "command": entry["command"]},
                )

        # 2. Custom Commands
        if custom_commands is not None:
            custom_node = node.add("Custom Commands", data={"type": "custom_folder"})
            for entry in custom_commands:
                custom_node.add_leaf(
                    f"{entry['name']} – {entry['description']}",
                    data={
                        "type": "custom_command",
                        "command": entry["command"],
                        "name": entry["name"],
                        "description": entry["description"]
                    }
                )

        # 3. Favorites (nur auf Root-Level)
        if node is self.root:
            fav_node = node.add("Favorites", data={"type": "favorites"})

            for fav in favorites:
                fav_node.add_leaf(
                    f"★ {fav['name']} – unknown description" if not fav.get("description") else f"★ {fav['name']} – {fav['description']}",
                    data={
                        "type": "custom_command" if fav.get("name") else "command",
                        "command": fav["command"],
                        "name": fav.get("name", ""),
                        "description": fav.get("description", "")
                    }
                )

            # Eigene Befehle
            if custom_commands:
                for cmd in custom_commands:
                    if is_fav(cmd, favorites):
                        fav_node.add_leaf(
                            f"★ {cmd['name']} – {cmd['description']}",
                            data={
                                "type": "custom_command",
                                "command": cmd["command"],
                                "name": cmd["name"],
                                "description": cmd["description"]
                            }
                        )

    def on_tree_node_expanded(self, event: Tree.NodeExpanded) -> None:
        node = event.node
        if node.data and node.data.get("type") in ["folder", "custom_folder"] and not node.children:
            if node.data.get("type") == "custom_folder":
                return
            self.load_nodes(node, node.data["children"])

    def on_tree_node_selected(self, event: Tree.NodeSelected) -> None:
        node = event.node
        if not node.data:
            return
        if node.data.get("type") in ["command", "custom_command"]:
            cmd: str = node.data["command"]
            copy_to_clipboard(cmd)
            self.app.copied_command = True
            self.app.exit()

class TermKitApp(App):
    TITLE = "TermKit"
    BINDINGS = [
        ("a", "add_command", "Add Command"),
        ("d", "delete_command", "Delete Command"),
        ("f", "toggle_favorite", "Favorite/Unfavorite"),
        ("q", "quit", "Quit"),
        ("/", "toggle_search", "Search"),
    ]
    copied_command = False
    in_search_mode = False

    def compose(self) -> ComposeResult:
        yield Header()
        self.search_input = Input(placeholder="Search...", id="search-bar")
        self.search_input.display = False
        yield self.search_input
        yield Container(CommandTree("Commands"), id="main-container")
        self.footer = Footer()
        yield self.footer
        self.footer_hint = Static("", id="custom-footer")
        yield self.footer_hint

    def on_mount(self) -> None:
        self.refresh_tree()
        self.update_footer()

    def refresh_tree(self):
        tree = self.query_one(CommandTree)
        tree.clear()
        tree.load_nodes(
            tree.root,
            load_platform_commands(),
            custom_commands=load_user_commands(),
            favorites=load_favorites()
        )
        tree.root.expand()
        self.set_focus(tree)

    def update_footer(self):
        if self.in_search_mode:
            self.footer_hint.update("Search active – type /exit to leave search")
        else:
            self.footer_hint.update("")

    def action_add_command(self):
        self.mount(AddCommandDialog(), before="#main-container")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        dialog = self.query_one(AddCommandDialog)
        if event.button.id == "cancel":
            dialog.remove()
            return
        if event.button.id == "add":
            name = dialog.query_one("#cmd_name", Input).value.strip()
            command = dialog.query_one("#cmd_command", Input).value.strip()
            desc = dialog.query_one("#cmd_desc", Input).value.strip()
            if not (name and command):
                return
            user_commands = load_user_commands()
            user_commands.append({
                "name": name,
                "command": command,
                "description": desc
            })
            save_user_commands(user_commands)
            dialog.remove()
            self.refresh_tree()

    def action_delete_command(self):
        tree = self.query_one(CommandTree)
        node = tree.cursor_node
        if node and node.data and node.data.get("type") == "custom_command":
            name = node.data["name"]
            user_commands = load_user_commands()
            user_commands = [c for c in user_commands if c["name"] != name]
            save_user_commands(user_commands)
            self.refresh_tree()

    def action_toggle_favorite(self):
        tree = self.query_one(CommandTree)
        node = tree.cursor_node
        if not node or not node.data:
            return

        if node.data.get("type") not in ["command", "custom_command"]:
            return

        cmd = node.data.get("command")
        label = str(node.label)
        name = label.split(" – ")[0].replace("★ ", "")
        desc = label.split(" – ")[1] if " – " in label else ""

        if not isinstance(cmd, str) or not cmd.strip():
            return

        favs = load_favorites()
        entry = {"name": name, "command": cmd, "description": desc}

        # ✅ Nur hinzufügen, wenn kein Custom Command
        if entry not in favs:
            if node.data.get("type") == "custom_command":
                return  # Hinzufügen blockieren
            favs.append(entry)
        else:
            # ✅ Entfernen immer erlauben
            favs.remove(entry)

        save_favorites(favs)
        self.refresh_tree()


    def action_toggle_search(self):
        self.search_input.display = not self.search_input.display
        self.in_search_mode = self.search_input.display
        self.update_footer()
        if self.search_input.display:
            self.set_focus(self.search_input)
            self.search_input.value = ""
        else:
            self.refresh_tree()

    def on_input_changed(self, event: Input.Changed) -> None:
        if event.input.id != "search-bar":
            return

        query = event.value.strip().lower()

        if query in ["/exit", "/q"]:
            self.search_input.display = False
            self.in_search_mode = False
            self.update_footer()
            self.refresh_tree()
            return

        tree = self.query_one(CommandTree)
        tree.clear()
        root = tree.root

        def matches(cmd):
            return query in cmd["name"].lower() or query in cmd.get("description", "").lower()

        for cat in load_platform_commands():
            for group in cat.get("children", []):
                for cmd in group.get("children", []):
                    if matches(cmd):
                        root.add_leaf(
                            f"{cmd['name']} – {cmd['description']}",
                            data={"type": "command", "command": cmd["command"]}
                        )

        for cmd in load_user_commands():
            if matches(cmd):
                root.add_leaf(
                    f"{cmd['name']} – {cmd['description']}",
                    data={
                        "type": "custom_command",
                        "command": cmd["command"],
                        "name": cmd["name"],
                        "description": cmd["description"]
                    }
                )

        root.expand()

if __name__ == "__main__":
    TermKitApp().run()
