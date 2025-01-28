import shutil
import subprocess
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
PYTHON_DIR = ROOT_DIR / 'kattis' / 'python'
NEW_PROBS_DIR = ROOT_DIR / 'new_probs'
README_FILE = ROOT_DIR / 'README.md'

# Ensure the target directory exists
assert PYTHON_DIR.exists(), "Directory for Python does not exist"

def move_new_problems():
    print("Checking and creating target directories...")
    for difficulty in ['1_Easy', '2_Medium', '3_Hard']:
        target_dir = PYTHON_DIR / difficulty
        target_dir.mkdir(parents=True, exist_ok=True)
        print(f"Directory ready: {target_dir}")

    print("Moving new problem files to their respective directories...")
    for problem_dir in NEW_PROBS_DIR.iterdir():
        if problem_dir.is_dir():
            for py_file in problem_dir.glob('*.py'):
                difficulty = py_file.parent.name  # e.g., 1_Easy
                target_dir = PYTHON_DIR / difficulty
                print(f"Moving {py_file.name} to {target_dir}")
                shutil.move(str(py_file), str(target_dir))
    print("File move complete.")

def update_readme():
    print("Updating README.md file...")
    with open(README_FILE, 'w') as f:
        f.write("# Kattis Solutions\n\n")
        f.write("This repository shares solutions to Kattis problems in Python. ")
        f.write("It's a mix of challenge and fun. ")
        f.write("Updates will come as I solve more problems. ")
        f.write("For corrections or suggestions, please contact me on Discord `plotsu`.\n\n")
        f.write("## Problems\n")
        f.write("| Problem | Difficulty | Language | Solution |\n")
        f.write("| ------- | ---------- | -------- | -------- |\n")

        # Loop through each difficulty folder (1_Easy, 2_Medium, 3_Hard)
        for difficulty_dir in sorted(PYTHON_DIR.iterdir()):
            if difficulty_dir.is_dir():
                # Extract just 'Easy' from '1_Easy' etc.
                difficulty = difficulty_dir.stem.split('_', 1)[-1]
                for file in sorted(difficulty_dir.glob('*.py')):
                    if file.is_file() and not file.name.startswith('.gitkeep'):
                        problem_name = file.stem
                        github_solution_url = (
                            f"https://github.com/ImPlotting/kattisol/blob/main/"
                            f"kattis/python/{difficulty_dir.name}/{file.name}"
                        )
                        kattis_problem_url = f"https://open.kattis.com/problems/{problem_name.lower()}"
                        f.write(
                            f"| [{problem_name}]({kattis_problem_url}) "
                            f"| {difficulty} "
                            f"| Python "
                            f"| [Solution]({github_solution_url}) |\n"
                        )
    print("README.md updated.")

def git_operations():
    print("Starting git operations...")
    subprocess.run(["git", "add", "."], check=True)
    # Commit only if there are changes
    status_result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    if not status_result.stdout.strip():
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
