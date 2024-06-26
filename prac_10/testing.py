"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car._odometer == 0, "Car does not set odometer correctly"

    # Assert statements to show if Car sets the fuel correctly
    # Test 1: Fuel set using the value passed in
    test_car = Car(fuel=10)
    assert test_car.fuel == 10, "Car does not set fuel correctly when value passed in"
    # Test 2: Fuel set using the default value
    test_car = Car()
    assert test_car.fuel == 0, "Car does not set fuel correctly using default value"


run_tests()

# Uncomment the following line and run the doctests
# (PyCharm may see your >>> doctest comments and run doctests anyway.)
doctest.testmod()


# Fix the failing is_long_word function
# (don't change the tests, change the function!)
# Fixed by changing the condition to >= instead of just >

def format_sentence(phrase):
    """Format a phrase as a sentence, starting with a capital and ending with a single full stop."""
    return phrase.capitalize() + '.'


# Run tests for format_sentence function
# Doctests
"""
>>> format_sentence('hello')
'Hello.'
>>> format_sentence('It is an ex parrot.')
'It is an ex parrot.'
>>> format_sentence('this is a test')
'This is a test.'
"""
