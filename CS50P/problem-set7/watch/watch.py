import re
import sys

"""
File: watch.py
Description:
    Extracting a YouTube video ID from an embedded YouTube video URL in an HTML string.

"""

def main():
    print(parse(input("HTML: ")))

def parse(s):
    pttr = r"src=\"https?://(?:www\.)?youtube\.com/embed/(\w+)\""
    matches = re.search(pttr, s)
    if matches:
        ret = "http://youtu.be/" + matches.group(1)
        return ret


if __name__ == '__main__':
    main()
