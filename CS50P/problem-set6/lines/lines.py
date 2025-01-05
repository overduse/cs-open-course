#!/usr/bin/env python3

"""
File: lines.py

Count Python Source lines of code, but does not taking
multi-line comments into consideration.

"""


import sys

def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) >2:
        sys.exit("Too many command-line arguments")

    if sys.argv[1][-3:] == ".py":
        file_name = sys.argv[1]
        print(file_name)
        try:
            code_lines = 0
            with open(file_name, 'r') as file:
                # line = file.readlines()
                for line in file:
                    stripped_line = line.strip()
                    if stripped_line and not stripped_line.startswith('#'):
                        code_lines += 1
            print(code_lines)
        except:
            sys.exit("File does not exist")

    else:
        sys.exit("Not a Python file")


if __name__ == '__main__':
    main()
