#!/usr/bin/env python3

"""
File: scourgify.py
Description:
    convert CSV file, "name, file" -> "first, last, house"

"""


import sys
import csv

def main():

    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-4:]!=".csv":
            sys.exit(f"Could not read {sys.argv[1]}")
        else:
            students = []
            with open(sys.argv[1], 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    students.append({"name": row["name"], "house": row["house"]})
            with open(sys.argv[2], 'w') as file:
                writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for student in students:
                    writer.writerow({"first": student["name"].split(',')[1].strip(),
                                    "last": student["name"].split(',')[0],
                                    "house": student["house"]})


if __name__ == '__main__':
    main()
