import subprocess

subprocess.run(
    [".venv/Scripts/black.exe", "--check", "src", "tests"],
    check=True,
)