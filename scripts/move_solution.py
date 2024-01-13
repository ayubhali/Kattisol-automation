import shutil
from pathlib import Path

# Set the root directory to the current directory where the script is located
ROOT_DIR = Path(__file__).resolve().parent.parent

# Define the path to the directory for C++ solutions
CPP_DIR = ROOT_DIR / 'Kattis' / 'C++'
NEW_PROBS_DIR = ROOT_DIR / 'new_probs'
README_FILE = ROOT_DIR / 'README.md'

# Ensure the C++ directory is correct
assert CPP_DIR.exists(), "Directory for C++ does not exist"

def move_new_problems():
    for difficulty in ['1_Easy', '2_Medium', '3_Hard']:
        target_dir = CPP_DIR / difficulty
        target_dir.mkdir(parents=True, exist_ok=True)

    # Move C++ problem files to the correct difficulty directory
    for problem_dir in NEW_PROBS_DIR.iterdir():
        if problem_dir.is_dir():
            for cpp_file in problem_dir.glob('*.cpp'):
                difficulty = cpp_file.parent.name
                target_dir = CPP_DIR / difficulty
                shutil.move(str(cpp_file), str(target_dir))
def update_readme():
    with open(README_FILE, 'w') as f:
        f.write("# Kattis Solutions\n\n")
        f.write("This repository is where I share solutions to problems from [Kattis](https://open.kattis.com/) as I learn C++. ")
        f.write("It's a mix of challenge and fun, and I'm excited to see where this journey takes me. ")
        f.write("Updates will come as I solve more problems. If a solution is wrong/incorrect or you would like to provide suggestions, ")
        f.write("please contact me on discord `plotsu`.\n\n")
        f.write("## Problems\n")
        f.write("| Problem | Difficulty | Language | Solution |\n")
        f.write("| ------- | ---------- | -------- | -------- |\n")
        
        # Only loop over the C++ directory
        for difficulty_dir in sorted(CPP_DIR.iterdir()):
            difficulty_display = difficulty_dir.stem.split('_')[1]
            for file in sorted(difficulty_dir.glob('*.cpp')):  # Process only .cpp files
                if file.is_file() and not file.name.startswith('.gitkeep'):  # Ignore .gitkeep files
                    problem_name = file.stem
                    github_solution_url = f"https://github.com/ImPlotting/Kattis-Solutions/blob/main/Kattis/C++/{difficulty_dir.stem}/{file.name}"
                    kattis_problem_url = f"https://open.kattis.com/problems/{problem_name.lower()}"
                    f.write(f"| [{problem_name}]({kattis_problem_url}) | {difficulty_display} | C++ | [Solution]({github_solution_url}) |\n")

if __name__ == "__main__":
    move_new_problems()
    update_readme()
