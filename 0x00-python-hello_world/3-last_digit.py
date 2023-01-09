#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
less_than = "and is less than 6 and not 0"
# Last digit of number is last_digit and is 0
# Last digit of number is last_digit and is greater than 5
if number < 0:
    last_digit = number % -10
else:
    last_digit = number % 10

if last_digit != 0 and last_digit < 6:
    print("Last digit of", number, "is", last_digit, less_than)
elif last_digit == 0:
    print("Last digit of", number, "is", last_digit, "and is 0")
else:
    print("Last digit of", number, "is", last_digit, "and is greater than 5")
