import os
import csv
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from subprocess import run

folder_path = "../visualise_cath_s60"
csv_file = os.path.join("S60_inspection_decisions.csv")

def view_image_get_decision(image_path, file_base):
    plt.figure(figsize=(15, 5))
    imgplot = plt.imshow(mpimg.imread(image_path))
    plt.axis('off')
    plt.tight_layout()
    plt.ion()
    plt.show()
    decision = get_user_decision(file_base)
    plt.close()
    return decision

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
        decision = input("Viewing {}.png. Enter your decision (1-accept, 2-reject, 0-no decision): ".format(file_base))
        if decision in ["1", "2", "0"]:
            return decision
        else:
            print("Invalid option. Please enter 1, 2, 0")

def main():
    decisions = read_existing_decisions()

    for file in sorted(os.listdir(folder_path)):
        if file.endswith("_combined.png"):
            file_base = file.replace("_combined.png", "")
            if file_base not in decisions:
                decision = view_image_get_decision(os.path.join(folder_path, file), file_base)
                decisions[file_base] = decision
                write_decision(decisions)

if __name__ == "__main__":
    main()