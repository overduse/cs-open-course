#!/usr/bin/env python3

"""
File: extensions.py
Description:
    input: file name.
    output: file type.

"""

def main():
    usr_input = input("File name: ")
    input_list = usr_input.strip().split('.')
    if(len(input_list)>=2):
        ext = input_list[-1].lower()
        if(ext == "jpeg" or ext == "jpg"):
            print("image/jpeg")
        elif(ext == "gif" or ext == "png"):
            print("image/", ext, sep="")
        elif(ext == "bin"):
            print("application/octet-stream")
        elif(ext == "pdf" or ext == "zip"):
            print("application/", ext, sep="")
        elif(ext == "txt"):
            print("text/plain")

    else:
        print("application/octet-stream")



if __name__ == '__main__':
    main()
