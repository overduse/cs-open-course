#!/usr/bin/env python3

"""
File: twttr.py

Removing vowels from input string.

"""

def main():
    s = input("Input: ").strip()
    print("Output: ", end="")
    output = shorten(s)
    print(output)

def shorten(word):
    ret = ""
    for c in word:
        if (c.lower() not in ['a', 'e', 'i', 'o', 'u']):
            ret += c
    return ret

if __name__ == '__main__':
    main()
