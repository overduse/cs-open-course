#!/usr/bin/env python3

"""
File: twttr.py
Description:
    remove all vowels from input string.

"""

def main():
    s = input("Input: ").strip()
    print("Output: ", end="")
    for c in s:
        if (c.lower() not in ['a', 'e', 'i', 'o', 'u']):
            print(c, end='')
    print('\n')


if __name__ == '__main__':
    main()
