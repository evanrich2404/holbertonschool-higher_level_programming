#!/usr/bin/python3
"""module for the Base class"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for the Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        with open((cls.__name__ + ".json"), "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                holddeez = [ii.to_dictionary() for ii in list_objs]
                f.write(Base.to_json_string(holddeez))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if dictionary:
            if cls.__name__ == "Rectangle":
                lammo = cls(1, 1)
            elif cls.__name__ == "Square":
                lammo = cls(1)
            lammo.update(**dictionary)
            return lammo

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename) as f:
                holddeez = Base.from_json_string(f.read())
                return [cls.create(**ii) for ii in holddeez]
        except IOError:
            return []
