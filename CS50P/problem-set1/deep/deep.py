#!/usr/bin/env python3

"""
File: deep.py
Description:
    a reply of the Answer to the Great Question of Life,
    the Universe, and Everything.

    “Forty-two,” said Deep Thought, with infinite majesty and calm.”
    -- The Hitchhiker’s Guide to the Galaxy, Douglas Adams

"""

def main():
    usr_input = input("What is the Answer to the Great Question"
                      " of Life, the Universe, and Everything? ")
    usr_input = usr_input.strip().lower()
    if(usr_input == '42' or
       usr_input == 'forty-two' or
       usr_input == 'forty two'):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
