#!/usr/bin/python3
'''defines a class square'''


class Square:
    ''' represent squar'''

    def __init__(self, size=0):
        '''inisializing
        Args:
            size (int): represent the size of class square.
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        '''square area method
        Return: current square area
        '''

        return self.__size **2
