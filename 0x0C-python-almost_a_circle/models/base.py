#!/usr/bin/python3
''' defines class rectangle '''

import json
import os


class Base:
    ''' Represent class base '''
    __nb_objects = 0
    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' Returns the JSON string representation '''
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' Writes the JSON string '''
        filenam = cls.__name__+'.json'
        a = []
        if list_objs is not None:
            for ele in list_objs:
                a.append(cls.to_dictionary(ele))
        with open(filenam, 'w') as f:
            f.write(cls.to_json_string(a))

    @staticmethod
    def from_json_string(json_string):
        ''' Returns the list of the JSON string '''
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        ''' Returns an instance with all attributes already set '''
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        ''' Returns a list of instances '''
        filename = cls.__name__+'.json'
        l_dictionaries = []
        l_isinstance = []

        if os.path,exist(filename):
            with open(filename) as f:
                l_dictionaries = cls.from_json_string(f.read())

                for dictionary in l_dictionaries:
                    l_isinstance.append(cls.create(**dictionary))

        return l_isinstance
