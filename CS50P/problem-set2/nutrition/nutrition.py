#!/usr/bin/env python3

"""
File: nutrition.py

show nutrition infomation for the 20 most frequently consumed
raw fruits, according to Food & Drug Adminstration (FDA)

"""

def main():

    usr_input = input("Item: ").strip().lower()

    if usr_input == 'apple':
        print("Calories: ", end="")
        print(130)
    elif usr_input == 'avocado':
        print("Calories: ", end="")
        print(50)
    elif usr_input == 'kiwifruit':
        print("Calories: ", end="")
        print(90)
    elif usr_input == 'pear':
        print("Calories: ", end="")
        print(100)
    elif usr_input == 'sweet cherries':
        print("Calories: ", end="")
        print(100)


if __name__ == '__main__':
    main()

