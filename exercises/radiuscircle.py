"""Write a Python program which accepts the radius of a circle from the user and compute the area."""

import math

RADIUS = float(input("What's the radius? "))

print("The area is {0}".format(math.pi * math.pow(RADIUS, 2)))
