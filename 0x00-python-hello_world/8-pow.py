#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b % 2 == 0:
        return pow(a * a, b / 2)
    elif b % 2 == 1:
        return a * pow(a * a, (b - 1) / 2)
    elif b < 0:
        return 1 / pow(a, -b)
    else:
        return a * pow(a, b - 1)
