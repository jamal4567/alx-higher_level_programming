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
        if attrs is None:
            return self.__dict__
        my_dic = {}
        for ele in attrs:
            try:
                my_dic[ele] = self.__dict__[ele]
            except:
                pass
        return my_dic

    def reload_from_json(self, json):
        '''eplaces all attributes of the Student instance '''
        for key, value in json.items():
            setattr(self, key, value)
