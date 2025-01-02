#!/usr/bin/env python3
from pyfiglet import Figlet
import sys
import random

"""
File: figlet.py
Description:
    generating ASCII art text using the 'pyfiglet' library.

"""


def main():
    figlet = Figlet()
    if len (sys.argv) <2:
        f = random.choice(figlet.getFonts())
    elif sys.argv[1]=='-f' and sys.argv[2] in figlet.getFonts():
        f = sys.argv[2]
    else:
        sys.exit("Invalid usage")

    figlet.setFont(font=f)
    s = input('Output: ').strip()
    print(figlet.renderText(s))


if __name__ == '__main__':
    main()
