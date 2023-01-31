#!/usr/bin/python3
"""module 11-student"""


class Student:
    """class Student that defines a student by: (based on 10-student.py)
    adds attrs to public method to_json and reload_from_json"""
    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Public method that retrieves a dictionary representation of a
        Student instance (same as 8-class_to_json.py)"""
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for i in attrs:
                if i in self.__dict__:
                    new_dict[i] = self.__dict__[i]
            return new_dict

    def reload_from_json(self, json):
        """Public method that replaces all attributes of the Student
        instance"""
        for i in json:
            self.__dict__[i] = json[i]
