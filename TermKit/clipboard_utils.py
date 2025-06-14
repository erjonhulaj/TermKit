import platform
import subprocess
import shutil

def copy_to_clipboard(text):
    system = platform.system()

    try:
        if system == "Darwin":
            # macOS – nutzt pbcopy
            subprocess.run("pbcopy", input=text.encode("utf-8"))
        elif system == "Windows":
            # Windows – nutzt clip.exe
            subprocess.run("clip", input=text.encode("utf-8"), shell=True)
        elif system == "Linux":
            # Linux – bevorzugt xclip oder xsel
            if shutil.which("xclip"):
                subprocess.run(["xclip", "-selection", "clipboard"], input=text.encode("utf-8"))
            elif shutil.which("xsel"):
                subprocess.run(["xsel", "--clipboard", "--input"], input=text.encode("utf-8"))
            else:
                raise Exception("No clipboard tool found on Linux (install xclip or xsel)")
        else:
            raise Exception(f"Unsupported OS: {system}")

        print("[✓] Command copied to clipboard.")
    except Exception as e:
        print(f"Clipboard error: {e}")
