import os
import csv
from PIL import Image
from subprocess import run

folder_path = "../visualise_cath_s60"
csv_file = os.path.join("S60_inspection_decisions.csv")

def view_image(image_path):
    with Image.open(image_path) as img:
        img.show()

def read_existing_decisions():
    if not os.path.exists(csv_file):
        return {}
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        return {rows[0]: rows[1] for rows in reader}

def write_decision(decisions):
    with open(csv_file, mode='w') as file:
        writer = csv.writer(file)
        for key, value in decisions.items():
            writer.writerow([key, value])

def get_user_decision(file_base):
    while True:
        decision = input(f"Viewing {file_base}.png. Enter your decision (1-accept, 2-reject, 0-no decision): ")
        if decision == "3":
            run(["pymol", os.path.join(folder_path, f"{file_base}.pse")])
            continue
        elif decision in ["1", "2", "0"]:
            return decision
        else:
            print("Invalid option. Please enter 1, 2, 0")

def main():
    decisions = read_existing_decisions()

    for file in sorted(os.listdir(folder_path)):
        if file.endswith("_combined.png"):
            file_base = file.replace("_combined.png", "")
            if file_base not in decisions:
                view_image(os.path.join(folder_path, file))
                decision = get_user_decision(file_base)
                decisions[file_base] = decision
                write_decision(decisions)

if __name__ == "__main__":
    main()