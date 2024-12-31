#!/usr/bin/env python3

"""
File: interpreter.py
Description:
    Calculate the result of binary arithmetic expression.

"""


def main():
    expression = input("Expression: ").strip()
    x, y, z = expression.split(' ')
    if(y=='+'):
        result = int(x) + int(z)
        print(f"{result:>.1f}")
    elif(y=='-'):
        result = int(x) - int(z)
        print(f"{result:>.1f}")
    elif(y=='*'):
        result = int(x) * int(z)
        print(f"{result:>.1f}")
    elif(y=='/'):
        result = float(x) / float(z)
        print(f"{result:>.1f}")


if __name__ == '__main__':
    main()
