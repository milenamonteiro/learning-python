"""Create a Python project to get the value of Pi to n number of decimal places."""

import math

PLACES = int(input("How many decimal places for pi? "))

print(round(math.pi, PLACES))
