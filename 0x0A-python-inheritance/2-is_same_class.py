#!/usr/bin/python3
''' defines function is_same_class '''


def is_same_class(obj, a_class):
    ''' Returns True if object is exactly an instance of the specified class
    otherwise False.
    '''
    if type(obj) == a_class:
        return True
    return False
