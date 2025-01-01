#!/usr/bin/env python3

"""
File: taqueria.py
Description:
    calculating the total of a customer's order based
    on a predefined menu.

"""

menu = {
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}

def main():
    sum = 0
    while True:
        try:
            usr_order = input("Item: ").strip().lower()
            sum += menu[usr_order]
            print(f"Total: ${sum:>.2f}")
        except KeyError:
            pass
        except:
            break


if __name__ == '__main__':
    main()
