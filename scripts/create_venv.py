import subprocess
import sys
from pathlib import Path

subprocess.run([sys.executable, "-m", "venv", ".venv"], check=True)

python = Path(".venv") / "Scripts" / "python.exe"

subprocess.run([str(python), "-m", "pip", "install", "--upgrade", "pip"], check=True)
subprocess.run([str(python), "-m", "pip", "install", "-r", "requirements-dev.txt"], check=True)