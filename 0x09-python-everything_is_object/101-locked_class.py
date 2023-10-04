#!/usr/bin/python3
''' defines class LockedClass '''


class LockedClass:
    ''' prevents the user ,
    from dynamically creating new instance attributes.
    '''
    __slots__ = ("first_name")
