import os
import subprocess

env = os.environ.copy()
env["PYTHONPATH"] = "src"

subprocess.run(
    [".venv/Scripts/pylint.exe", "src"],
    env=env,
    check=True,
)