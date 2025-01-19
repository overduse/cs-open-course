from datetime import date
import sys

def main():

    usr_input = get_birthday()
    print(display_mins(usr_input))


def get_birthday():
    entry = input("Date of Birth: ")
    return load_birthday(entry)


def load_birthday(birthday):
    try:
        return date.fromisoformat(birthday)
    except ValueError:
        sys.exit("Incorrect value entered")


def display_mins(birthday):
    import inflect
    p = inflect.engine()

    tdy = date.today()
    mins = (tdy - birthday).days * 1440
    ret = p.number_to_words(mins, andword="").capitalize() + " " + p.plural_noun("minute", mins)
    return ret


if __name__ == "__main__":
    main()
