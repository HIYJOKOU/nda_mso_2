import os
import subprocess

env = os.environ.copy()
env["PYTHONPATH"] = "src"

subprocess.run(
    [".venv/Scripts/pytest.exe", "tests", "-v"],
    env=env,
    check=True,
)