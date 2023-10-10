#!/usr/bin/python3
"""Module represent class student"""


class Student:
    ''' class student '''

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' Retrieves a dictionary representation of a Student'''
        _dic = {}
        if attrs is None:
            return self.__dict__
        for ele in attrs:
            try:
                _dic[ele] = self.__dict__[ele]
            except:
                pass
        return _dic
