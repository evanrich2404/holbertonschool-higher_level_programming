#!/usr/bin/python3
"""
takes in a URL and an email, sends POST request to passed URL with email
as a parameter, and displays body of response
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
