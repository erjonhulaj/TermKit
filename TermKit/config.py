import platform
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def get_platform():
    return platform.system()

def load_platform_commands():
    system = get_platform()
    file = BASE_DIR / ("commands_mac.json" if system == "Darwin" else "commands_win.json")
    with open(file, "r") as f:
        return json.load(f)

def load_user_commands():
    file = BASE_DIR / "user_commands.json"
    if Path(file).exists():
        with open(file, "r") as f:
            return json.load(f)
    return []

def save_user_commands(commands):
    file = BASE_DIR / "user_commands.json"
    with open(file, "w") as f:
        json.dump(commands, f, indent=2)
