import json
import shutil
from pathlib import Path

# Set the root directory to the current directory where the script is located
ROOT_DIR = Path(__file__).resolve().parent.parent

# Define the path to the directories for C99 and Cpp solutions
C99_DIR = ROOT_DIR / 'Kattis' / 'C99'
CPP_DIR = ROOT_DIR / 'Kattis' / 'Cpp'
NEW_PROBS_DIR = ROOT_DIR / 'new_probs'
README_FILE = ROOT_DIR / 'README.md'

def move_new_problems():
    for difficulty in ['1_Easy', '2_Medium', '3_Hard']:
        for lang_dir in [C99_DIR, CPP_DIR]:
            prob_dir = lang_dir / difficulty
            prob_dir.mkdir(parents=True, exist_ok=True)

    for problem in NEW_PROBS_DIR.iterdir():
        if problem.is_dir():
            difficulty = problem.name.split('_')[0]
            for lang_dir in problem.iterdir():
                if lang_dir.is_dir() and lang_dir.name in ['C', 'Cpp']:
                    target_dir = C99_DIR if lang_dir.name == 'C' else CPP_DIR
                    target_dir = target_dir / difficulty
                    shutil.move(str(lang_dir), str(target_dir))
                    info = {
                        'name': problem.name,
                        'difficulty': difficulty,
                        'language': lang_dir.name
                    }
                    with open(target_dir / lang_dir.name / 'info.json', 'w') as f:
                        json.dump(info, f, indent=4)

def update_readme():
    with open(README_FILE, 'w') as f:
        f.write("# Kattis Solutions\n")
        f.write("Solutions to the Kattis problems.\n\n")
        f.write("## Problems\n")
        f.write("| Problem | Difficulty | Language |\n")
        f.write("| ------- | ---------- | -------- |\n")
        for lang_dir in [C99_DIR, CPP_DIR]:
            language = 'C' if 'C99' in str(lang_dir) else 'Cpp'
            for difficulty_dir in lang_dir.iterdir():
                difficulty = difficulty_dir.stem.split('_')[1]  # Extract difficulty from folder name
                for problem_dir in difficulty_dir.iterdir():
                    problem_name = problem_dir.stem  # Extract problem name from folder name
                    if (problem_dir / 'info.json').exists():
                        # Load info from the existing info.json file
                        with open(problem_dir / 'info.json') as info_file:
                            info = json.load(info_file)
                    else:
                        # Create a new info dictionary if info.json does not exist
                        info = {
                            'name': problem_name,
                            'difficulty': difficulty,
                            'language': language
                        }
                    # Write the problem information to the README
                    f.write(f"| [{info['name']}]({problem_dir}) | {info['difficulty']} | {info['language']} |\n")

if __name__ == "__main__":
    move_new_problems()
    update_readme()
