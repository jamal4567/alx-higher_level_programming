#!/usr/bin/python3
'''
module with function that print name
'''


def say_my_name(first_name, last_name=""):
    ''' function that prints first_name and last_name
    Args:
        first_name: argument 1
        last_name: argument 2
    Raises:
        TypeError: if Args not a string
    '''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
