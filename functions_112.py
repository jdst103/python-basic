from math import pi
# The task is to create a Functional calculator#
# We need it to be able to add, subtract, divide amd multiply

#Define an add function
def add(num1, num2):
    return num1 + num2

#Define an subtract function
def subtract(num1, num2):
    return num1 - num2

#Define an multiply function
def multiply(num1, num2):
    return num1 * num2

#define a divide function
def divide(num1, num2):
    return num1 / num2

#define a are_of_circle function for radius
def area_of_circle_radius(radius):
    return pi * (radius**2)

#define a are_of_circle function for diameter
def area_of_circle_diameter(diameter):
    radius = diameter / 2
    return pi * (radius**2)

#define a area_of_square function
def area_of_square(width, height):
    return width * height

# define an area_of_triangle - right angle triangle

def area_of_triangle(width, height):
    return 0.5 * width * height
