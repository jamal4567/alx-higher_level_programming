#!/usr/bin/python3
'''
modul with one function that add 2 integers
'''


def add_integer(a, b=98):
    ''' Return an integer the addition of a and b

    Args:
        a : argument1
        b : argument2

    Raises:
        TypeError: if a or b not integer or float
    '''

    if (not isinstance(a, int) and not isinstance(a, float)):
        raise("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise("b must be an integer")
    return (int(a) + int(b))
