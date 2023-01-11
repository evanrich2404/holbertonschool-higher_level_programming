#!/usr/bin/python3
for asci in range(ord('a'), ord('z')+1):
    notasci = chr(asci)
    if notasci not in [('e'), ('q')]:
        print(notasci, end="")
        [".format("]
