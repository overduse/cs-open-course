#!/usr/bin/env python3
import emoji

"""
File: emojize.py
Description:
    taking user input as a string, and converts any emoji aliases (e.g., ":smile:")
    into the corresponding emoji characters.

"""


def main():

    usr_input = input("Input: ").strip()
    print("Output:", emoji.emojize(usr_input, language='alias'))


if __name__ == '__main__':
    main()
