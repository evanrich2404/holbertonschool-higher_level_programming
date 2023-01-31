#!/usr/bin/python3
"""
module contains the function load_from_json_file
"""


def load_from_json_file(filename):
    """creates an Object from a “JSON file”"""
    import json
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
