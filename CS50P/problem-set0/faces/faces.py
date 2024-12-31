#!/usr/bin/env python3

"""
File: faces.py
Description:
    receiving input from user, replacing ':)' with
    smiling emoji and replacing ':(' with sad face.

"""

def main():
    usr_intput = input()
    usr_intput = usr_intput.replace(':)', '🙂')
    usr_intput = usr_intput.replace(':(', '🙁')
    print(usr_intput)

if __name__ == '__main__':
    main()
