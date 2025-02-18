# Anthony Towery
# February 18th, 2025
# P2LAB1
# Using math expressions and formatting float values

# import math module to use the constant, math.pi

import math

radius = float(input("What is the radius of the circle? "))

print()
    
diameter = radius *2

circumference =2 * radius * math.pi

area = math.pi * math.pow(radius,2)
print(f'The diameter of the circle is {diameter:.1f}\n')
print(f'The circumference of the circle is {circumference:.2f}\n')
print(f'The area of the circle is {area:.3f}\n')


##print()
##print()
##print(f'Diameter: {diameter:25.1f}\n')
##print(f'Circumference: {circumference:25.2f}\n')
##print(f'Area: {area:25.3f}\n')
