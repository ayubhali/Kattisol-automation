import subprocess
from pathlib import Path

# Path to the main repo folder (parent of the 'scripts' folder)
ROOT_DIR = Path(__file__).resolve().parent.parent

# Points to: kattisol/Kattis/Python
PYTHON_DIR = ROOT_DIR / 'Kattis' / 'Python'

# Where to write the new README
README_FILE = ROOT_DIR / 'README.md'

def update_readme():
    """Create or overwrite README.md with a table of Python solutions."""
    if not PYTHON_DIR.exists():
        raise FileNotFoundError(f"[Error] Directory does not exist: {PYTHON_DIR}")

    with open(README_FILE, 'w') as f:
        f.write("# Kattis Solutions\n\n")
        f.write("This repository shares solutions to Kattis problems in Python. ")
        f.write("It’s a mix of challenge and fun. Updates will come as more problems are solved.\n\n")

        # Table header
        f.write("## Problems\n")
        f.write("| Problem | Difficulty | Language | Solution |\n")
        f.write("| ------- | ---------- | -------- | -------- |\n")

        # Loop through each difficulty folder (1_Easy, 2_Medium, 3_Hard)
        for diff_dir in sorted(PYTHON_DIR.iterdir()):
            if diff_dir.is_dir():
                # Extract just the difficulty text, e.g., 'Easy' from '1_Easy'
                diff_name = diff_dir.name.split('_', 1)[-1]
                
                # Find all .py solutions
                for py_file in sorted(diff_dir.glob('*.py')):
                    problem_name = py_file.stem
                    kattis_url = f"https://open.kattis.com/problems/{problem_name.lower()}"
                    github_url = (
                        # Update the GitHub username/repo as needed
                        f"https://github.com/ImPlotting/kattisol/blob/main/"
                        f"Kattis/Python/{diff_dir.name}/{py_file.name}"
                    )
                    f.write(
                        f"| [{problem_name}]({kattis_url}) "
                        f"| {diff_name} "
                        f"| Python "
                        f"| [Solution]({github_url}) |\n"
                    )

def git_operations():
    """Stage, commit, and push README and any other changes."""
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Auto update of problem solutions"], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)

def main():
    update_readme()
    git_operations()

if __name__ == "__main__":
    main()
