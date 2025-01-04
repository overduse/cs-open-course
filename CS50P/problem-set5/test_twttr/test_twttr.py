from twttr import shorten

"""
File: test_twttr.py

catches (corner cases):
    - without vowel replacement
    - without capitalized vowel replacement
    - without lowercase vowel replacement
    - omitting numbers
    = printing in uppercase
    - punctuation
"""


def test_shorten():
    assert shorten("Hello, world!") == "Hll, wrld!"
    assert shorten("HELLO, WORLD!") == "HLL, WRLD!"
    assert shorten("1234aeiou") == "1234"
    assert shorten("!@#$%^&*AEIOU") == "!@#$%^&*"
