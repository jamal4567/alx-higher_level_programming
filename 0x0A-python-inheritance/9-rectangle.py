#!/usr/bin/python3
''' Implement BaseGeometry '''
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    ''' represent class Rectangle '''
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        ''' area of rectangle '''
        return self.__width * self.__height

    def _str_(self):
        ''' Retutn rectangle description '''
        return ("[Rectangle]" + str(self.__width) + "/" + str(self.__height))
