#!/usr/bin/python3
''' Implement Rectangle '''
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    ''' square class '''
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.size = size
