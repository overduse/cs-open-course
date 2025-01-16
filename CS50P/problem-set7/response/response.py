import validators

"""
file: response.py
Description:
  This script validates an email address input by the
  user and returns whether it is valid or invalid.

"""


def main():
    content = input("What's your email address? ")
    print(is_valid(content))


def is_valid(s):
    val = validators.email(s)
    if val:
        ret = "Valid"
    else:
        ret = "Invalid"
    return ret


if __name__ == '__main__':
    main()
