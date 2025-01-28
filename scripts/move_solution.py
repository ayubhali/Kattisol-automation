import shutil
import subprocess
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
PYTHON_DIR = ROOT_DIR / 'kattis' / 'python'
NEW_PROBS_DIR = ROOT_DIR / 'new_probs'
README_FILE = ROOT_DIR / 'README.md'

def move_new_problems():
    print("Checking and creating target directories...")
    difficulties = ['1_Easy', '2_Medium', '3_Hard']
    for diff in difficulties:
        folder = PYTHON_DIR / diff
        folder.mkdir(parents=True, exist_ok=True)
        print(f"Directory ready: {folder}")

    print("Moving new problem files to their respective directories...")

    # If .py files are directly in new_probs, move them to 1_Easy by default
    for py_file in NEW_PROBS_DIR.glob('*.py'):
        default_dir = PYTHON_DIR / '1_Easy'
        print(f"Moving {py_file.name} to {default_dir}")
        shutil.move(str(py_file), str(default_dir))

    # If there are subfolders in new_probs (e.g., 1_Easy), move files accordingly
    for sub_dir in NEW_PROBS_DIR.iterdir():
        if sub_dir.is_dir():
            difficulty = sub_dir.name  # e.g., '1_Easy'
            target_dir = PYTHON_DIR / difficulty
            target_dir.mkdir(parents=True, exist_ok=True)
            for py_file in sub_dir.glob('*.py'):
                print(f"Moving {py_file.name} to {target_dir}")
                shutil.move(str(py_file), str(target_dir))

    print("File move complete.")

def update_readme():
    print("Updating README.md...")
    with open(README_FILE, 'w') as f:
        f.write("# Kattis Solutions\n\n")
        f.write("This repository shares solutions to Kattis problems in Python.\n\n")
        f.write("## Problems\n")
        f.write("| Problem | Difficulty | Language | Solution |\n")
        f.write("| ------- | ---------- | -------- | -------- |\n")

        # Loop each difficulty folder (1_Easy, 2_Medium, 3_Hard, etc.)
        for diff_dir in sorted(PYTHON_DIR.iterdir()):
            if diff_dir.is_dir():
                # Convert '1_Easy' -> 'Easy'
                parts = diff_dir.name.split('_', 1)
                difficulty = parts[1] if len(parts) == 2 else diff_dir.name

                for py_file in sorted(diff_dir.glob('*.py')):
                    problem_name = py_file.stem
                    kattis_url = f"https://open.kattis.com/problems/{problem_name.lower()}"
                    github_url = (
                        f"https://github.com/ImPlotting/kattisol/blob/main/"
                        f"kattis/python/{diff_dir.name}/{py_file.name}"
                    )
                    f.write(
                        f"| [{problem_name}]({kattis_url}) "
                        f"| {difficulty} "
                        f"| Python "
                        f"| [Solution]({github_url}) |\n"
                    )
    print("README.md updated.")

def git_operations():
    print("Starting git operations...")
    subprocess.run(["git", "add", "."], check=True)

    # Check if there's anything to commit
    status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    if not status.stdout.strip():
        print("No changes to commit.")
        return

    subprocess.run(["git", "commit", "-m", "Auto update of problem solutions"], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)
    print("Git operations completed.")

def main():
    move_new_problems()
    update_readme()
    git_operations()

if __name__ == "__main__":
    main()
