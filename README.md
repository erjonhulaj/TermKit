# TermKit

**TermKit** is a cross-platform terminal toolkit for macOS and Windows.  
It shows an interactive, categorized menu of useful system commands — copied to your clipboard instead of being executed directly.

🖥️ Stop googling commands. Just launch TermKit, navigate, and copy.

---

## 🎬 Demo

![TermKit Demo](assets/termkit-demo.gif)

---

## 📦 Downloads

| Platform | File |
|----------|------|
| macOS    | [Download termkit-mac.zip](https://github.com/erjonhulaj/TermKit/releases/download/v1.0.0/termkit-mac.zip) |
| Windows  | [Download termkit-win.zip](https://github.com/erjonhulaj/TermKit/releases/download/v1.0.0/termkit-win.zip) |

---

## ✅ Features

- Clean Textual-based TUI
- Arrow-key navigation (↑ ↓ + Enter)
- System, Network, Development, Custom categories
- Commands are copied.
- Extendable with your own custom commands
- Favorites
- Search
- Works offline after setup

---

## ⚙️ Requirements

- **Python 3.10+** must be installed
  - macOS: via [Homebrew](https://brew.sh) or [python.org](https://www.python.org/downloads/)
  - Windows: via [python.org](https://www.python.org/downloads/windows/)
- Internet is needed only for first-time setup (to install `textual`)

---

## 🚀 Installation

### macOS

1. Download and unzip `termkit-mac.zip`
2. Open the extracted folder and double-click `setup.command`
3. If macOS blocks the file:
   - Go to **System Preferences → Security & Privacy → General**
   - Click **“Open Anyway”** for `setup.command`
   - Confirm the prompt
4. The installer will:
   - Install TermKit to `~/.termkit`
   - Install the required Python packages (if needed)
   - Create a terminal command: `tk`

Now you can open any terminal and type:

```sh
tk
```

### Windows

1. Download and unzip `termkit-win.zip`  
2. Run `install.bat` by double-clicking it  
3. The aliases `tk` `termkit` will be added to your `PATH`  
4. Open any terminal (CMD or PowerShell) and run:

```bat
tk
termkit
```

### 🔧 How to Use

Launch **TermKit**:

- **macOS:** `tk`
- **Windows:** `tk` `termkit`

**Navigation**

| Key          | Action                          |
|--------------|---------------------------------|
| **Enter**           | Enter category                  |
| ↑ / ↓        | Move between items              |
| **Enter**    | Copy command to clipboard       |
| **Cmd/Ctrl + V**    | Manually paste into your terminal |
| **q**      | Quit                            |
| **a**      | Add custom command                            |
| **d**      | Delete custom command                            |
| **f**      | Add/Delete favorite                            |
| **/**      | Search                           |

---

### 💡 Why TermKit?

TermKit is ideal for:

- Developers, sysadmins, power users, and learners  
- Saving time by browsing real-world terminal commands    
- Staying organized with a visual shell command menu  

---

## 📃 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

© 2025 Erjon Hulaj

---

### 🤝 Contribute

This project was built for personal use but is open to ideas & feedback.

Made by **Erjon Hulaj**

---

Note: This project is not related to the legacy TermKit by @unconed (2011).



