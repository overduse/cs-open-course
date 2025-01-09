#!/usr/bin/env python3

"""
File: shirt.py

Download shirt.py:
wget https://cs50.harvard.edu/python/2022/psets/6/shirt/shirt.png

Download input files:
wget https://cs50.harvard.edu/python/2022/psets/6/shirt/muppets.zip

unzip input zip file:
unzip muppets.zip


Description:
    Overlay shirt.png on input file.

"""


import sys
import os
from PIL import Image, ImageOps

def main():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        file_before = sys.argv[1]
        file_output = sys.argv[2]
        input_ext = os.path.splitext(file_before)[1]
        output_ext = os.path.splitext(file_output)[1]
        ext_list = ('.jpg', '.jpeg', '.png')

        if not (input_ext in ext_list or
                output_ext in ext_list):
            sys.exit("Invalid input")
        elif input_ext != output_ext:
            sys.exit("Input and output have different extensions")
        else:
            img_before = Image.open(file_before)
            shirt = Image.open("shirt.png")
            img_fit = ImageOps.fit(img_before, shirt.size)
            img_fit.paste(shirt, shirt)
            img_fit.save(file_output)


if __name__ == '__main__':
    main()
