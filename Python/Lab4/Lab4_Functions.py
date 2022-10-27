import os

def ex_1(given_path):
    return sorted({os.path.splitext(f)[-1] for f in os.listdir(given_path) if os.path.splitext(f)[-1] != ''})

def ex_2(directory_path, file_path):
    with open(file_path, "w") as fd:
        [fd.write(os.path.abspath(f) + '\n') for f in os.listdir(directory_path) if f.startswith("a") and os.path.splitext(f)[-1] != '']