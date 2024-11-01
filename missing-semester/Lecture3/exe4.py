#!/usr/bin/env python3

# To practice using Vim, re-do this 
# Demo from lecture on your own machine
import sys

def fizz_buzz(limit):
    for i in range(1, limit+1):
        if i%3==0 and i%5==0:
            print('fizz')
            print('buzz')
        elif i%3==0 or i%5==0:
            print('fizz')
        else:
            print(i)

def main():
    fizz_buzz(int(sys.argv[1]))


if __name__ == '__main__':
    main()
