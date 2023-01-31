#!/usr/bin/python3
"""
module contains the save_to_json_file function
"""


def save_to_json_file(my_obj, filename):
    """writes an object to a text file using JSON representation"""
    import json
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
