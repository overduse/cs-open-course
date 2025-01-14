from working import convert
import pytest

"""
File: test_working.py
Description:
    Takeing a time range in the 12-hour format (AM/PM)
    and converts it to the 24-hour format.

"""


def test_convert_normal():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_convert_corner():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"

def test_convert_to():
    with pytest.raises(ValueError):
        convert("12 AM - 12 PM")

def test_convert_range():
    with pytest.raises(ValueError):
        convert("13:00 AM to 11:60 PM")
