# Samuel Abling
# 02/17/2025
# P2LAB1
# This program receives the radius of a circle from user, then calculates the diameter, circumference, and area of that circle.


# Import math library

import math


# User inputs radius. Calculate diameter, circumference, and area from radius, assign to variables.

pi = math.pi
radius = float(input('\nWhat is the radius of the circle? '))
diameter = 2 * radius
circumference = 2 * pi * radius
area = pi * (radius ** 2)


# Display diameter, circumference, and area

print(f'\nThe diameter of the circle is {diameter:.1f}')
print(f'\nThe circumference of the circle is {circumference:.2f}')
print(f'\nThe area of the circle is {area:.3f}\n')