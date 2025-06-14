# TermKit

**TermKit** is a cross-platform terminal toolkit for macOS and Windows.  
It shows an interactive, categorized menu of useful system commands — copied to your clipboard instead of being executed directly.

🖥️ Stop googling commands. Just launch TermKit, navigate, and copy.

---

## 📦 Downloads

| Platform | File |
|----------|------|
| macOS    | `termkit-mac.zip` |
| Windows  | `termkit-win.zip` |

---

## ✅ Features

- Clean Textual-based TUI
- Arrow-key navigation (↑ ↓ + Enter)
- System, Network, Development, Custom categories
- Commands are *copied*, not executed (safety first!)
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
3. The alias `tk` will be added to your `PATH`  
4. Open any terminal (CMD or PowerShell) and run:

```bat
tk
```

### 🔧 How to Use

Launch **TermKit**:

- **macOS:** `tk`
- **Windows:** `tk`

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

### 📃 LICENCE

This project is licensed under the  
**Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License (CC BY-NC-ND 4.0)**  
👉 <https://creativecommons.org/licenses/by-nc-nd/4.0/>

You are free to:

- ✅ **Use and modify** TermKit for personal, non-commercial purposes

You may **not**:

- ❌ Use TermKit or its code for commercial use  
- ❌ Publish modified versions or reuse parts of the code  
- ❌ Create derivatives or spin-offs  

> © 2025 Erjon Hulaj. All rights reserved.

---

### 🤝 Contribute

This project was built for personal use but is open to ideas & feedback.  

Made by **Erjon Hulaj**




