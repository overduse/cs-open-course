#!/usr/bin/env python3

months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

def main():

    while True:
        try:
            usr_input = input("Date: ").strip()
            if '/' in usr_input:
                mm = int(usr_input.split('/')[0])
                dd = int(usr_input.split('/')[1])
                yyyy = int(usr_input.split('/')[2])
            elif ',' in usr_input:
                mm = months[usr_input.split(' ')[0]]
                dd = int(usr_input.split(' ')[1].split(',')[0])
                yyyy = int(usr_input.split(' ')[2])
            else:
                raise ValueError

            if mm>12 or dd>30:
                raise ValueError

        except (ValueError, KeyError):
            pass

        else:
            print(f"{yyyy}-{mm:02}-{dd:02}")
            break

if __name__ == '__main__':
    main()
