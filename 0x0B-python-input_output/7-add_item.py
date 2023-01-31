#!/usr/bin/python3
"""
module contains a script that adds all arguments to a Python list,
and then save them to a file
It uses save_to_json_file and load_from_json_file
list must be saved as a JSON representation in a file named add_item.json
if the file doesn’t exist, it should be created
"""
__import__('5-save_to_json_file').save_to_json_file()
__import__('6-load_from_json_file').load_from_json_file()


def add_item():
    """ adds all arguments to a Python list, and then save them to a file """
    import sys
    import os.path
    if os.path.exists('add_item.json'):
        my_list = load_from_json_file('add_item.json')
    else:
        my_list = []
    for i in range(1, len(sys.argv)):
        my_list.append(sys.argv[i])
    save_to_json_file(my_list, 'add_item.json')
