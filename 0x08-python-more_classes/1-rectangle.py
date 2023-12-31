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
