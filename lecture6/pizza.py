import sys
import csv
from tabulate import tabulate

if len(sys.argv) != 2:
    sys.exit("Too few command-line arguments")

if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        headers = next(reader)
        rows = list(reader)
        print(tabulate(rows, headers=headers, tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")