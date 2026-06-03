#main.py

from data import SRC_DIR
import subprocess
import sys


if __name__ == "__main__":
    try:
        file =SRC_DIR / "web_presentation.py"
        subprocess.run([sys.executable, "-m", "streamlit", "run", str(file)])
    except Exception as e :
        print(f"An error occurred: {e}")