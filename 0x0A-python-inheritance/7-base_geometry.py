#!/usr/bin/python3
''' defines class BaseGeometry '''


class BaseGeometry:
    ''' Represent BaseGeometry '''
    def area(self):
        ''' method with no implementation '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ''' method that validates value
        Args:
            name: name alway string
            value: value to validate
        Raises:
            TypeError: if it's not an integer
            ValueError: if value less or equal to zero.
        '''
        self.name = name
        self.value = value
        
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
