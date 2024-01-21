#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if number < 0:
    number = -number

last_digit = number % 10
if last_digit < 0:
    last_digit = -(last_digit)

if last_digit > 5:
    msg = "and is greater than 5"
elif last_digit == 0:
    msg = "and is 0"
else:
    msg = "and is less than 6 and not 0"
print("Last digit of {:d} is {:d}".format(number, last_digit), msg)
