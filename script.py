import os
import pathlib
import random

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def create_dir(name: str):
    pathlib.Path(os.getcwd() + f"/{name}").mkdir(parents=True, exist_ok=True)


def create_file(dir: str):
    with open(dir, "w") as f_p:
        f_p.write("Model; Output value; Time of computation;\n")
        model = random.choice(["A", "B", "C"])
        value = random.randrange(1001)
        time = random.randrange(1001)
        f_p.write(f"{model}; {value}; {time}s;")


def compute_time(model: str, path: str):
    sum = 0
    for root, dirs, files in os.walk(path, topdown=True):
        dirs[:] = [d for d in dirs if d not in ["venv", ".idea"]]
        if len(files) > 0:
            for file in files:
                with open(root + '/' + file, "r") as sol_file:
                    all_lines = sol_file.readlines()
                    sec_splitted = all_lines[1].split(';')
                    if sec_splitted[0] == "A":
                        sum += int(sec_splitted[2][:-1])
    return sum


def main():
    for day in days:
        create_dir(day)
        for t in ['morning', 'evening']:
            create_dir(f"{day}/{t}")
            create_file(f"{day}/{t}/Solutions.csv")
    print(compute_time("A", os.getcwd()))


main()