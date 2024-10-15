import shutil
import subprocess
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

CPP_DIR = ROOT_DIR / 'Kattis' / 'C++'
NEW_PROBS_DIR = ROOT_DIR / 'new_probs'
README_FILE = ROOT_DIR / 'README.md'

assert CPP_DIR.exists(), "Directory for C++ does not exist"

def move_new_problems():
    print("Checking and creating target directories...")
    for difficulty in ['1_Easy', '2_Medium', '3_Hard']:
        target_dir = CPP_DIR / difficulty
        target_dir.mkdir(parents=True, exist_ok=True)
        print(f"Directory ready: {target_dir}")
        print("Moving new problem files to their respective directories...")
        
    for problem_dir in NEW_PROBS_DIR.iterdir():
        if problem_dir.is_dir():
            for cpp_file in problem_dir.glob('*.cpp'):
                difficulty = cpp_file.parent.name
                target_dir = CPP_DIR / difficulty
                print(f"Moving {cpp_file.name} to {target_dir}")
                shutil.move(str(cpp_file), str(target_dir))
    print("File move complete.")

def update_readme():
    print("Updating README.md file...")
    with open(README_FILE, 'w') as f:
        f.write("# Kattis Solutions\n\n")
        f.write("This repository shares solutions to Kattis problems in C++.")
        f.write("It's a mix of challenge and fun. ")
        f.write("Updates will come as I solve more problems. ")
        f.write("For corrections or suggestions, please contact me on Discord `plotsu`.\n\n")
        f.write("## Problems\n")
        f.write("| Problem | Difficulty | Language | Solution |\n")
        f.write("| ------- | ---------- | -------- | -------- |\n")

        for difficulty_dir in sorted(CPP_DIR.iterdir()):
            difficulty = difficulty_dir.stem.split('_')[1]
            for file in sorted(difficulty_dir.glob('*.cpp')):
                if file.is_file() and not file.name.startswith('.gitkeep'):
                    problem_name = file.stem
                    github_solution_url = f"https://github.com/ImPlotting/Kattis-Solutions/blob/main/Kattis/C++/{difficulty_dir.stem}/{file.name}"
                    kattis_problem_url = f"https://open.kattis.com/problems/{problem_name.lower()}"
                    f.write(f"| [{problem_name}]({kattis_problem_url}) | {difficulty} | C++ | [Solution]({github_solution_url}) |\n")
    print("README.md updated.")

def git_operations():
    print("Starting git operations...")
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Auto update of problem solutions"], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)
    print("Git operations completed.")

if __name__ == "__main__":
    move_new_problems()
    update_readme()
    git_operations()

