#!/usr/bin/env python3

"""
File: bank.py

Home Federal Savings Bank, give $100 to anyone who isn't
greeted with a "hello." and starts with an 'h', will receive $20.

"""


def main():
    usr_input = input("Greeting: ")
    gain = value(usr_input)
    print(gain)


def value(greeting):

    greeting = greeting.lower().lstrip()
    if (len(greeting)>=5 and greeting[:5]=="hello" and
       (len(greeting)==5 or (greeting[5] == ' ' or greeting[5] == ','))):
        ret = 0
    elif greeting[0] == 'h':
        ret = 20
    else:
        ret = 100
    return ret

if __name__ == '__main__':
    main()
