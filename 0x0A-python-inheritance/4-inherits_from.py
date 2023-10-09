#!/usr/bin/python3
''' defines function  inherits_from'''


def inherits_from(obj, a_class):
    ''' function for checking object
    Args:
       obj: object to check
       a_class: class
    Return:
       True or False
    '''
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
