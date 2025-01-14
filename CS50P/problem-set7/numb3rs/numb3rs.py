import re
import sys

"""
File: numb3rs.py
Description:
    A script to validate an IPv4 address.

"""

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ip = ip.strip()
    matches = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
    flag = False
    if matches:
        flag = True
        if int(matches.group(1))<0 or int(matches.group(1))>255:
            flag = False

        if int(matches.group(2))<0 or int(matches.group(2))>255:
            flag = False

        if int(matches.group(3))<0 or int(matches.group(3))>255:
            flag = False

        if int(matches.group(4))<0 or int(matches.group(4))>255:
            flag = False

    return flag


if __name__ == '__main__':
    main()
