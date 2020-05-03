import pytest

# Import the function convert_to_int()
from preprocessing_helpers import convert_to_int

# Complete the unit test name by adding a prefix
def test_on_string_with_one_comma():
    assert convert_to_int("2,018") == 2018

def test_on_string_with_one_comma_new():
    return_value = convert_to_int("2,018")
    assert isinstance(return_value, int)
    assert return_value == 2018