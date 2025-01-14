import re
import sys

"""
File: working.py
Description:
    Converting a given time range from 12-hour format (AM/PM) to 24-hour format.

"""


def main():
    print(convert(input("Hour: ")))

def convert(s):
    pttr = r"^([\d:]+)\s(AM|PM)\sto\s([\d:]+)\s(AM|PM)"
    matches = re.search(pttr, s)
    if matches:
        if ':' in matches.group(1):
            hour_start = int(matches.group(1).split(':')[0])
            min_start = int(matches.group(1).split(':')[1])
            if min_start not in range(60):
                raise ValueError
        else:
            hour_start = int(matches.group(1))
            min_start = 0

        if hour_start not in range(13):
            raise ValueError


        if ':' in matches.group(3):
            hour_end = int(matches.group(3).split(':')[0])
            min_end = int(matches.group(3).split(':')[1])
            if min_end not in range(60):
                raise ValueError
        else:
            hour_end = int(matches.group(3))
            min_end = 0

        if hour_end not in range(13):
            raise ValueError

        if matches.group(2)=="PM":
            if hour_start != 12:
                hour_start = hour_start+12
        else:
            if hour_start == 12:
                hour_start = 0

        if matches.group(4)=="PM":
            if hour_end != 12:
                hour_end = hour_end + 12
        else:
            if hour_end == 12:
                hour_end = 0

        ret = f"{hour_start:02}:{min_start:02} to {hour_end:02}:{min_end:02}"
        return ret

    else:
        raise ValueError


if __name__ == '__main__':
    main()
