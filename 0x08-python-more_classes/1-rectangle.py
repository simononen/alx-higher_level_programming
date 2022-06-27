#!/usr/bin/python3
'''
Module to work with rectangles
'''


class Rectangle:
    '''
    Represents 2D four sided Polygon with two set of equal sides
    '''
    def __init__(self, width=0, height=0):
        '''Initialize Rectangle with given width and height
        Args:
            width (int): Width of the rectangle
            height (int): Position of the rectangle
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Retrieve width of Rectangle
        Returns:
            int: width of Rectangle
        '''
        return self.__width

    @property
    def height(self):
        '''Retrieve height of Rectangle
        Returns:
            int: height of Rectangle
        '''
        return self.__height

    @width.setter
    def width(self, value):
        '''Update width of Rectangle
        Args:
            value (int): New width of Rectangle
        '''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        else:
            if value < 0:
                raise ValueError('width must be >= 0')
            else:
                self.__width = value

    @height.setter
    def height(self, value):
        '''Update height of Rectangle
        Args:
            value (int): New height of Rectangle
        '''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        else:
            if value < 0:
                raise ValueError('height must be >= 0')
            else:
                self.__height = value
