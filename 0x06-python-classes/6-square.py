#!/usr/bin/python3
'''defines a class square'''


class Square:
    ''' represent squar'''

    def __init__(self, size=0, position=(0, 0)):
        '''inisializing
        Args:
            size (int): represent the size of class square.
            position (int, int): represent position of square
        '''

        self.size = size
        self.position = position

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

    @property
    def position(self):
        '''retrive the size '''

        return (self.__position)

    @position.setter
    def position(self, value):
        ''' set position of squar
        Args:
            value (int): tupl
        '''
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        '''square area method
        Return: current square area
        '''

        return (self.__size ** 2)

    def my_print(self):
        ''' print square with # character'''
        if self.size == 0:
            print('')
            return
        for i in range(self.position[1]):
            print("")
        for j in range(self.size):
            for k in range(self.position[0]):
                print(' ',end="")
            for l in range(self.size):
                print('#', end="")
            print()
