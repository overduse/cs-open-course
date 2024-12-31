#!/usr/bin/env python3

"""
File: camel.py
Description:
    transform camel case to snake case.
    camelCase -> camel_case

"""


def main():
    usr_input = input("camelCase: ").strip()
    print("snake_case: ", end="")
    for c in usr_input:
        if(c.isupper()):
            print('_', end='')
            print(c.lower(), end='')
        else:
            print(c, end='')
    print('\n')


if __name__ == '__main__':
    main()
