#!/usr/bin/python3
''' defines function is_same_class '''


def is_kind_of_class(obj, a_class):
    ''' 
    Args:
        obj: object to check
        a_class: class
    Return:
        True if the object is an instance of,
        class that inherited from,the specified class 
    otherwise False.
    '''
    return isinstance(obj, a_class)
