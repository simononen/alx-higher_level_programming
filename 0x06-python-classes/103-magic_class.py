#!/usr/bin/python3
'''Module with the Python class definition of a bytecode.'''
import math


class MagicClass:
    '''Represent an object for working with circles'''
    def __init__(self, radius=0):
        '''Initialize magic class'''
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('Radius must be a number')
        self.__radius = radius

    def area(self):
        '''Compute Area of this circle'''
        return self.__radius ** 2 * math.pi

    def circumference(self):
        '''Compute Circumference of this circle'''
        return 2 * math.pi * self.__radius
