import sys
import csv

if len(sys.argv) != 3:
    sys.exit("Usage: python scourgify.py input.csv output.csv")

try:
    students = []
    with open(sys.argv[1]) as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            last, first = row["name"].split(", ")
            students.append({"first": first, "last": last, "house": row["house"]})
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

with open(sys.argv[2], "w", newline="") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
    writer.writeheader()
    for student in students:
        writer.writerow(student)