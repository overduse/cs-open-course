#!/usr/bin/env python3

import emoji

def main():

    usr_input = input("Input: ").strip()
    print("Output:", emoji.emojize(usr_input, language='alias'))


if __name__ == '__main__':
    main()
