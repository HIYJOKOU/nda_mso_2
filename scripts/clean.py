import shutil
from pathlib import Path

shutil.rmtree(".venv", ignore_errors=True)
shutil.rmtree(".pytest_cache", ignore_errors=True)

for path in Path(".").rglob("__pycache__"):
    shutil.rmtree(path, ignore_errors=True)

for path in Path(".").rglob("*.pyc"):
    path.unlink(missing_ok=True)