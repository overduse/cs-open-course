#!/usr/bin/env python3

"""
File: faces.py
Description:
    receiving input from user, replacing ':)' with
    smiling emoji and replacing ':(' with sad face.

"""

def main():
    usr_input = input()
    usr_input = usr_input.replace(':)', '🙂')
    usr_input = usr_input.replace(':(', '🙁')
    print(usr_input)

if __name__ == '__main__':
    main()
