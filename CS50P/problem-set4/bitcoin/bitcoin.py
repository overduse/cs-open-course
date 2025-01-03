#!/usr/bin/env python3
import sys
import requests

"""
File: bitcoin.py
Description:
    receiving a float from sys.argv[1] float,
    returning the price of the num of bitcoin
    by using coindesk api.
"""


def main():

    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    else:
        try:
            num_coin = float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")

    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    # print(r.status_code)
    # print(type(r))
    # print(r.json())
    # print(r.text)

    content_json = r.json()
    # print(content_json['bpi']['USD']['rate_float'])
    rate_float = content_json['bpi']['USD']['rate_float']
    amount = num_coin * rate_float
    print(f"${amount:,.4f}")

if __name__ == '__main__':
    main()
