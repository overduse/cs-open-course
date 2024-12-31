#!/usr/bin/env python3

"""
File: coke.py
Description:
    Stimulating a vending machine process
    for purchasing a Coke.

"""


def main():
    amount = 50
    while amount > 0:
        print(f"Amount Due: {amount}")
        x = input("Insert Coin: ")
        if int(x)==25 or int(x)==10 or int(x)==5:
            amount -= int(x)
    print(f"Change Owed: {-amount}")


if __name__ == '__main__':
    main()
