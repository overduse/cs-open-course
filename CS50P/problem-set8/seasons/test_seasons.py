import pytest
from datetime import date
from seasons import get_birthday, load_birthday, display_mins

def test_seasons():
    assert display_mins(date.today()) == "Zero minutes"
