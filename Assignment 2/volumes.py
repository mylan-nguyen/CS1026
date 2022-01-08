#import the math library
import math

#define the function to find the volume of a cylinder
def volume_of_cylinder(radius, height):
    volume = math.pi * (radius ** 2) * height
    return volume

#define the function to find the volume of a rectangular prism
def volume_of_prism(length, width, height):
    volume = length * width * height
    return volume

#define the function to find the volume of an sphere
def volume_of_sphere(radius_sphere):
    volume = 4/3 * math.pi * radius_sphere
    return volume
