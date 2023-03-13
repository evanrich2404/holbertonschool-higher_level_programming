#!/usr/bin/python3
"""
takes in a letter and sends POST request to
http://0.0.0.0:5000/search_user with letter as a parameter
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})

    if r.headers.get('content-type') != 'application/json':
        print("Not a valid JSON")
    elif r.json() == {}:  # if r.json() is empty
        print("No result")
    else:
        print("[{}] {}".format(r.json().get('id'), r.json().get('name')))
