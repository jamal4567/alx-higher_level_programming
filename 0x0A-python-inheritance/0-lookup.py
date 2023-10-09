#!/usr/bin/python3
''' module with function lookup() '''


def lookup(obj):
    ''' Return the list of available,
    attributes and methods of an object
    '''
    return dir(obj)
