#!/usr/bin/env python3
import inflect

"""
File: adieu.py
Description:
    the script prints a farewell message in the format:
    "Adieu, adieu, to [name1], [name2], [name3], ..."

"""

def main():

    p = inflect.engine()
    input_list = []
    while True:
        try:
            usr_input = input("Name: ").strip()
            input_list.append(usr_input)
        except:
            if len(input_list)>0:
                content = "Adieu, adieu, to " + p.join(input_list)
                print(content)
            break

if __name__ == '__main__':
    main()
