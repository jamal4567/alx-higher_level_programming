#!/usr/bin/python3
''' defines class rectangle '''

from models.base import Base


class Rectangle(Base):
    ''' Represent class rectangle '''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        ''' get value of width '''
        return self.__width
    
    @property
    def height(self):
        ''' get value of height '''
        return self.__height
    
    @property
    def x(self):
        ''' get value of x '''
        return self.__x
    
    @property
    def y(self):
        ''' get value of y '''
        return self.__y
    
    @width.setter
    def width(self, value):
        '''set value of width '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        
        self.__width = value

    @height.setter
    def height(self, value):
        ''' set value of height '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        
        self.__height = value
    
    @x.setter
    def x(self, value):
        ''' set value of x '''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        
        self.__x = value

    @y.setter
    def y(self, value):
        ''' set value of y '''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        
        self.__y = value
    
    def area(self):
        ''' returns the area value of the Rectangle '''
        return self.__width * self.__height

    def display(self):
        ''' returns the area value of the Rectangle with # '''
        for y in range(self.__y):
            print()
        for row in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for column in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        ''' return format '''
        desc = '[Rectangle]' + ' (' + str(self.id) + ') '
        desc += str(self.__x)  + '/' + str(self.__y)
        desc += ' - ' + str(self.__width) + '/' + str(self.__height)
        return desc

    def update(self, *args, **kwargs):
        ''' assigns an argument to each attribute '''
        if args and len(args) != 0:
            count = 0
            for arg in args:
                if count == 0:
                    self.id = arg
                elif count == 1:
                    self.width = arg
                elif count == 2:
                    self.height = arg
                elif count == 3:
                    self.x = arg
                elif count == 4:
                    self.y = arg
                count += 1
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
    
    def to_dictionary(self):
        ''' returns the dictionary representation of a Rectangle '''
        dictionary = {'id':self.id, 'width':self.__width,
                      'height':self.__height, 'x':self.__x,
                      'y':self.__y}
        return dictionary
