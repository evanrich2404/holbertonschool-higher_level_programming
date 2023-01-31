#!/usr/bin/python3
"""
module 10-student that defines a student by: (based on 9-student.py)
adds attrs to public method to_json
"""


class Student:
    """class Student that defines a student by: (based on 9-student.py)
    adds attrs to public method to_json"""
    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Public method that retrieves a dictionary representation of a
        Student instance (same as 8-class_to_json.py)"""
        if type(attrs) == list:
            if all(type(attr) == str for attr in attrs):
                return {ii: getattr(self, ii)
                        for ii in attrs if hasattr(self, ii)}
        else:
            return new_dict

