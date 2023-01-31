#!/usr/bin/python3
"""
this module contains a function that returns an object
represented by a JSON string
"""


def from_json_string(my_str):
    """returns an object represented by a JSON string"""
    import json
    return json.loads(my_str)
