#!/usr/bin/env python3

"""
File: test_fuel.py
Description:
    stimulating fuel gauge system.
    divided into three parts:
      - main()
      - convert(fraction)
      - gauge(percentage)

"""

def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        else:
            gauge(percentage)
            break

def convert(fraction):
    x = int(fraction.split('/')[0])
    y = int(fraction.split('/')[1])
    if y == 0:
        raise ZeroDivisionError
    if x>y:
        raise ValueError()
    ret = round(1.0*x/y *100)
    return ret

def gauge(percentage):
    if percentage <=1:
        str = 'E'
    elif percentage >=99:
        str = 'F'
    else:
        str = f"{percentage}%"
    return str


if __name__ == '__main__':
    main()
