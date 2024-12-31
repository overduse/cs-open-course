#!/usr/bin/env python3

"""
receiving integer input m, and calculate energy
according to E=mc^2.

"""

def main():
    m = input()
    c = 3e8
    e = int(m) * int(c) ** 2
    print(e)

if __name__ == '__main__':
    main()
