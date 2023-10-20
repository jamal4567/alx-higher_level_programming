#!/usr/bin/python3
''' defines class square '''

from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Represent class square '''
    def __init__(self, size, x=0, y=0, id=None):
        self.__size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        ''' det value of size '''
        return self.width

    @size.setter
    def size(self, value):
        ''' set value of size '''
        self.width = value
        self.height = value

    def __str__(self):
        ''' Return string format '''
        string = '[Square]' + ' (' + str(self.id) + ') '
        string += str(self.x) + '/' + str(self.y)
        string += ' - ' + str(self.size)
        return string

    def update(self, *args, **kwargs):
        ''' Assign an argument to each attribute '''
        if args and len(args) != 0:
            count = 0
            for arg in args:
                if count == 0:
                    self.id = arg
                elif count == 1:
                    self.size = arg
                elif count == 2:
                    self.x = arg
                elif count == 3:
                    self.y = arg
                count += 1
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        ''' Return the dictionary representation of square '''
        dictionary = {'id': self.id, 'size': self.__size,
                      'x': self.x,
                      'y': self.y}
        return dictionary
