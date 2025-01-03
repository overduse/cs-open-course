#!/usr/bin/env python3
import random

"""
File: game.py
Description:
    Guessing Game.

"""

def generate_num():
    while True:
        try:
            lv = int(input("Level: "))
            # print(lv)
            if lv < 1:
                raise ValueError
        except ValueError:
            pass
        else:
            break
    return random.randint(1, lv)

def guess(choose_num):
    while True:
        # geuss_num = int()
        try:
            guess_num = int(input("Guess: "))
            if guess_num < 0:
                raise ValueError
            if guess_num > choose_num:
                print("Too large!")
            elif guess_num < choose_num:
                print("Too small!")
            else:
                print("Just right!")
                break
        except ValueError:
            pass

def main():

    choose_num = generate_num()
    guess(choose_num)


if __name__ == '__main__':
    main()
