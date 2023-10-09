#!/usr/bin/python3
''' defines function is_same_class '''


def is_kind_of_class(obj, a_class):
    ''' check objet
    Args:
        obj: object to check
        a_class: class
    Return:
        True or False.
    '''
    return isinstance(obj, a_class)
