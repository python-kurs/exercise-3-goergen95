# Exercise 3
from pathlib import Path
import csv
# import functions from utils here


data_dir = Path("B:/python_uni/exercise-3-goergen95/data/")
output_dir = Path("B:/python_uni/exercise-3-goergen95/solution")

# 1. Contstruct the path to the text file in the data directory using the `pathlib` module [2P]
path_txt = data_dir / "cars.txt"

# 2. Read the text file [2P]
with open(path_txt) as file:
    lines = [line.rstrip() for line in file]


# 3. Count the occurences of each item in the text file [2P]
uniqueCars = list(set(lines))    
    
number = []
for cars in uniqueCars:
    number.append(lines.count(cars))

# 4. Using `pathlib` check if a directory with name `solution` exists and if not create it [2P]
if not output_dir.exists():
    output_dir.mkdir(parents=True, exist_ok=True)

# 5. Write the counts to the file `counts.csv` in the `solution` directory in the format (first line is the header): [2P]
#    item, count
#    item_name_1, item_count_1
#    item_name_2, item_count_2
#    ...
    
carDic = dict(zip(uniqueCars,number))
counts = output_dir / "counts.csv"

with open(counts, 'w') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames =["item","count"])
    writer.writeheader()
    writer = csv.writer(csv_file)
    for key, value in carDic.items():
       writer.writerow([key, value])