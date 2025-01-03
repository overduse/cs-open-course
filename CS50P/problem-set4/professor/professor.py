#!/usr/bin/env python3
import random

"""
File: professor.py
Description:
    Achieving Little Professor.

"""

def main():
    lv = get_level()
    correct_num = 0
    for _ in range(10):
        X, Y = generate_integer(lv),  generate_integer(lv)
        tries = 0
        while True:
            try:
                usr_input = int(input(f"{X} + {Y} = "))
                if usr_input == X + Y:
                    correct_num += 1
                    break
                else:
                    tries += 1
                    print("EEE")
                    if tries == 3:
                        print(f"{X} + {Y} = {X+Y}")
                        break
                    raise ValueError
            except ValueError:
                pass

    print("Score:", correct_num)


def get_level():
    while True:
        try:
            lv_input = int(input("Level: ").strip())
            if not lv_input in [1, 2, 3]:
                raise ValueError
        except ValueError:
            pass
        else:
            return lv_input

def generate_integer(level):
    if level == 1:
        start = 0
    else:
        start = 10**(level-1)
    end = 10**level-1
    # print(start, end)
    return random.randint(start, end)


if __name__ == '__main__':
    main()
