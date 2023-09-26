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
    @property
    def size(self):
        ''' retrive the size '''
        return (self.__size)
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''square area method
        Return: current square area
        '''

        return (self.__size ** 2)
