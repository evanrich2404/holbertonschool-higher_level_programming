#!/usr/bin/python3
for num1 in range(0, 10):
    for num2 in range(1, 10):
        # this makes sure the numbers don't repeat
        if (num1 >= num2):
            continue
        # this makes sure it ends at 89
        elif (num1 == 8 and num2 == 9):
            print("{}{}".format(num1, num2))
        # this makes sure it prints the numbers, and in the correct format
        else:
            print("{}{}".format(num1, num2), end=", ")