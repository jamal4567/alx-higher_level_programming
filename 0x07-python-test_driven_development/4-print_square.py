#!/usr/bin/python3
'''
module with function that print square
'''


def print_square(size):
    ''' defines square for printing # character
    Args:
        size: length of the square
    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
        TypeError: if size is flaot and less than 0
    '''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print('#', end="")
        print()
