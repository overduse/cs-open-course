#!/usr/bin/env python3

"""stimulating fuel gauge system.

"""

def main():

    while True:
        try:
            usr_input = input("Fraction: ")
            x = int(usr_input.split('/')[0])
            y = int(usr_input.split('/')[1])
            if x>y:
                raise ValueError()
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        else:
            result = round(1.0*x/y *100)

            if result <=1:
                print('E', end='')
            elif result>=99:
                print('F', end='')
            else:
                print(f"{result}%")
            break


if __name__ == '__main__':
    main()
