#!/usr/bin/python3
"""class Student that defines a student by:"""


class Student:
    """class Student that defines a student by:"""
    def __init__(self, first_name, last_name, age):
        """Public instance attributes:"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """that retrieves a dictionary representation"""
        if attrs is None:
            return self.__dict__
        else:
            my_dict = {}
            for i in attrs:
                if hasattr(self, i):
                    my_dict[i] = getattr(self, i)
            return my_dict

    def reload_from_json(self, json):
        """that replaces all attributes of the Student instance:"""
        for key, value in json.items():
            setattr(self, key, value)
