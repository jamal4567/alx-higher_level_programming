#!/usr/bin/python3
''' Define classe rectangle '''


class Rectangle:
    ''' class define by:'''
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        ''' Instantiation
        Args:
            width: argument for width of rectangle
            height: argument for height of rectangle
        Raises:
              TypeError: if Args not integer
              ValueError: if Args less than 0
        '''
        type(self).number_of_instances += 1
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
        if self.__width == 0 or self.__height == 0:
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
                try:
                    print += str(self.print_symbol)
                except Exception:
                    print += type(self).print_symbol
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
        type(self).number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        ''' returns the biggest rectangle based on the area
        Args:
            rect_1: Rectangle 1
            rect_2: Rectangle 2
        Raises:
            TypeError: if not instance of Rectangle
        '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        ''' Return  a new Rectangle instance '''
        return cls(size, size)
