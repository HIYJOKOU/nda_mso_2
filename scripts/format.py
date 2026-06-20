import subprocess

subprocess.run(
    [".venv/Scripts/black.exe", "src", "tests"],
    check=True,
)