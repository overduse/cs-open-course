#!/usr/bin/env python3

"""
File: grocery.py
Description:
    prompting the user to input grocery items.

"""

def main():
    book = {}
    while True:
        try:
            usr_order = input().strip().upper()
            if usr_order in book:
                book[usr_order] += 1
            else:
                book.update({usr_order: 1})
        except:
            break
    for key in sorted(book):
        print(f"{book[key]} {key}")


if __name__ == '__main__':
    main()
