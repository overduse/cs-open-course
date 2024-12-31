#!/usr/bin/env python3

"""
File: meal.py

input: time.
output: what to eat when.

"""

def main():
    usr_input = input("What time is it? ").strip()
    hrs = convert(usr_input)
    if(hrs>=7 and hrs<=8):
        print("breakfast time")
    elif(hrs>=12 and hrs<=13):
        print("lunch time")
    elif(hrs>=18 and hrs<=19):
        print("dinner time")

def convert(time):
    hrs=int(time.split(' ')[0].split(':')[0])
    mins=int(time.split(' ')[0].split(':')[1])
    if(time.split(' ')[-1]=="p.m."):
        hrs += 12
    hrs = hrs + float(mins/60.0)
    return hrs


if __name__ == '__main__':
    main()
