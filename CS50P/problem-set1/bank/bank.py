#!/usr/bin/env python3

"""
File: bank.py
Description:
    Home Federal Savings Bank, give $100 to anyone who isn't greeted
    with a "hello." and starts with an 'h', will receive $20.

"""


def main():
    usr_input = input("Greeting: ").lower().lstrip()
    if(len(usr_input)>=5 and usr_input[:5]=="hello" and
       len(usr_input)==5 or (usr_input[5]==' ' or usr_input[5]==',')):
        print("$0")
    elif(usr_input[0]=='h'):
        print("$20")
    else:
        print("$100")


if __name__ == '__main__':
    main()
