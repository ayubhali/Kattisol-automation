import shutil
from pathlib import Path

# Set the root directory to the current directory where the script is located
ROOT_DIR = Path(__file__).resolve().parent.parent

# Define the path to the directory for C++ solutions
CPP_DIR = ROOT_DIR / 'Kattis' / 'C++'
NEW_PROBS_DIR = ROOT_DIR / 'new_probs'
README_FILE = ROOT_DIR / 'README.md'

# Ensure the C++ directory is correct
assert CPP_DIR.exists(), f"Directory {CPP_DIR} does not exist"

def move_new_problems():
    # Iterate over each difficulty directory in new_probs and move files accordingly
    for difficulty_dir in NEW_PROBS_DIR.iterdir(): 
        if difficulty_dir.is_dir():
            # Map the directory names to the corresponding difficulty in the C++ directory
            difficulty_map = {
                'Easy': '1_Easy',
                'Medium': '2_Medium',
                'Hard': '3_Hard'
            }
            target_difficulty = difficulty_map.get(difficulty_dir.name)
            if target_difficulty:
                # Move each .cpp file to the correct difficulty directory in C++
                for problem_file in difficulty_dir.glob('*.cpp'):
                    target_dir = CPP_DIR / target_difficulty
                    target_dir.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(problem_file), str(target_dir))

def update_readme():
    with open(README_FILE, 'w') as f:
        f.write("# Kattis Solutions\n\n")
        f.write("This repository contains solutions to various programming problems from the Kattis problem archive, primarily focused on C++.\n\n")
        f.write("## Problems\n")
        f.write("| Problem | Difficulty | Language | Solution |\n")
        f.write("| ------- | ---------- | -------- | -------- |\n")
        
        # Loop only over the C++ directory
        for difficulty_dir in sorted(CPP_DIR.iterdir()):
            difficulty_display = difficulty_dir.stem.replace('1_', 'Easy').replace('2_', 'Medium').replace('3_', 'Hard')
            for file in sorted(difficulty_dir.glob('*.cpp')):
                if file.is_file():
                    problem_name = file.stem
                    github_solution_url = f"https://github.com/ImPlotting/Kattis-Solutions/blob/main/Kattis/C++/{difficulty_display}/{file.name}"
                    kattis_problem_url = f"https://open.kattis.com/problems/{problem_name.lower()}"
                    f.write(f"| [{problem_name}]({kattis_problem_url}) | {difficulty_display} | C++ | [Solution]({github_solution_url}) |\n")

if __name__ == "__main__":
    move_new_problems()
    update_readme()