#!/usr/bin/python3
"""
module contains a script that adds all arguments to a Python list,
and then save them to a file
It uses save_to_json_file and load_from_json_file
list must be saved as a JSON representation in a file named add_item.json
if the file doesn’t exist, it should be created
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    """rocking the main"""
    try:
        my_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        my_list = []
    my_list.extend(sys.argv[1:])
    save_to_json_file(my_list, "add_item.json")
