#!/usr/bin/env python3

"""
File: pizza.py
Download CSV files:
wget https://cs50.harvard.edu/python/2022/psets/6/pizza/sicilian.csv
wget https://cs50.harvard.edu/python/2022/psets/6/pizza/regular.csv

Description:
    receive CSV file path as command-line argument,
    print grid style tabulate table.

"""

import sys
import csv
from tabulate import tabulate

def main():

    if len(sys.argv)<2:
        sys.exit("Too few command-line argument")
    elif len(sys.argv)>2:
        sys.exit("Too many command-line argument")
    else:
        if sys.argv[1][-4:] != ".csv":
            sys.exit("Not a CSV file")
        else:
            try:
                with open(sys.argv[1], 'r') as file:
                    reader = csv.reader(file)
                    headers = next(reader)
                    data = [row for row in reader]
                    print(tabulate(data, headers=headers, tablefmt='grid'))

            except FileNotFoundError:
                sys.exit("File does not exist")


if __name__ == '__main__':
    main()
