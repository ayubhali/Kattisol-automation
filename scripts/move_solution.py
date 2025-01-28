import subprocess
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
PYTHON_DIR = ROOT_DIR / 'kattis' / 'python'
README_FILE = ROOT_DIR / 'README.md'

def update_readme():
    if not PYTHON_DIR.exists():
        raise FileNotFoundError(f"Directory does not exist: {PYTHON_DIR}")

    with open(README_FILE, 'w') as f:
        f.write("# Kattis Solutions\n\n")
        f.write("This repository shares solutions to Kattis problems in Python.\n\n")
        f.write("## Problems\n")
        f.write("| Problem | Difficulty | Language | Solution |\n")
        f.write("| ------- | ---------- | -------- | -------- |\n")

        for diff_dir in sorted(PYTHON_DIR.iterdir()):
            if diff_dir.is_dir():
                difficulty = diff_dir.name
                for py_file in sorted(diff_dir.glob("*.py")):
                    problem_name = py_file.stem
                    kattis_url = f"https://open.kattis.com/problems/{problem_name.lower()}"
                    github_url = (
                        f"https://github.com/ImPlotting/kattisol/blob/main/"
                        f"kattis/python/{difficulty}/{py_file.name}"
                    )
                    f.write(
                        f"| [{problem_name}]({kattis_url}) "
                        f"| {difficulty} "
                        f"| Python "
                        f"| [Solution]({github_url}) |\n"
                    )

def git_operations():
    # Stage all changes
    subprocess.run(["git", "add", "."], check=True)
    
    # Check for changes
    status_result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    git_status = status_result.stdout.strip()

    # If there's nothing to commit, skip the commit step
    if not git_status:
        print("No changes to commit. Working tree clean.")
        return

    # Otherwise, commit and push
    subprocess.run(["git", "commit", "-m", "Auto update of solutions"], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)

def main():
    update_readme()
    git_operations()

if __name__ == "__main__":
    main()
