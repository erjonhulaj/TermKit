from textual_app import TermKitApp
import platform

def main():
    print("TermKit starting...")
    app = TermKitApp()
    app.run()
    if getattr(app, "copied_command", False):
        system = platform.system()
        paste_hint = "Cmd+V" if system == "Darwin" else "Ctrl+V"
        print(f"\nCommand copied to clipboard. Press {paste_hint} to paste it in your terminal.\n")

if __name__ == "__main__":
    main()
