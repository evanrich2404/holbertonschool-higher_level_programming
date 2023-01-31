#!/usr/bin/python3
"""module to read a text file(UTF8) and print it to stdout"""


def read_file(filename=""):
    """function to read a text file(UTF8) and print it to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
