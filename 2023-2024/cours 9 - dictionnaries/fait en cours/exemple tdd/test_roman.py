import pytest

from roman import to_roman


def test_to_roman_for_1():
    number = 1
    expected = "I"
    actual = to_roman(number)
    assert expected == actual


def test_to_roman_for_2():
    number = 2
    expected = "II"
    actual = to_roman(number)
    assert expected == actual


def test_to_roman_for_3():
    number = 3
    expected = "III"
    actual = to_roman(number)
    assert actual == expected


def test_to_roman_should_not_accept_negatives():
    number = -1
    with pytest.raises(ValueError):
        to_roman(number)
