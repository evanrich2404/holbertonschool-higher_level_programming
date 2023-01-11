#!/usr/bin/python3
def islower(c):
    for asci in range(ord('a'), ord('z'), ord('A'), ord('Z')):
        if c[asci] == (ord('a'), ord('z')):
            return True
        else:
            return False
