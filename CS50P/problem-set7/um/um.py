import re
import sys

"""
File: um.py
Description:
  Taking a string input and counts the number of times the word
  "um" appears as a standalone word, case-insensitively.

"""


def main():
    print(count(input("Text: ")))

def count(s):

    pttr = r"\bum\b"
    matches = re.findall(pttr, s, re.IGNORECASE)
    cnt = len(matches)
    return cnt


if __name__ == '__main__':
    main()
