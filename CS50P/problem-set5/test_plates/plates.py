#!/usr/bin/env python3

"""
File: plates.py
Description:
    Validing a vanity license plate.

"""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s)<2 or len(s)>6:
        return False
    idx_num = 0;
    for c in s:
        if c.isalpha():
            idx_num+=1
        else:
            break
    if idx_num == len(s):
        ret = True
    elif len(s[:idx_num])>=2 and s[idx_num:].isdecimal():
        if s[idx_num] != '0':
            ret = True
        else:
            ret = False
    else:
        ret = False
    return ret


if __name__ == '__main__':
    main()
