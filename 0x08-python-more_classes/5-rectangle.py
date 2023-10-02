#!/usr/bin/python3
''' Define classe rectangle '''


class Rectangle:
    ''' class define by: '''
    def __init__(self, width=0, height=0):
        ''' Instantiation
        Args:
            width: argument for width of rectangle
            height: argument for height of rectangle
        Raises:
              TypeError: if Args not integer
              ValueError: if Args less than 0
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        ''' retrive width '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' set width '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        ''' retrive height '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' set height '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        ''' return area of rectangle '''
        return self.__width * self.__height

    def perimeter(self):
        ''' return perimetr of rectangle '''
        if self.__width == 0 or self.__width == 0:
            return 0
        return (2 * (self.__width + self.__height))
    
    def __str__(self):
        ''' print the rectangle with the character #
        using str and print
        '''
        if self.__width == 0 or self.__height == 0:
            return ""
        print = ''
        for i in range(self.__height):
            for j in range(self.__width):
                print += '#'
            if i < self.__height - 1:
                print += '\n'
        return print

    def __repr__(self):
        ''' return a string representation of the rectangle '''
        re = "Rectangle(" + str(self.__width)
        re += ", " + str(self.__height) + ")"
        return re

    def __del__(self):
        ''' Print the message  when an instance of Rectangle is deleted'''
        print('Bye rectangle...')
