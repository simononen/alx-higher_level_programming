#!/usr/bin/python3
"""
Module to work with Rectangles
"""


class Rectangle:
    """Represent 2D Polygon with four perpendicular sides
    """
    def __init__(self, width=0, height=0):
        """Initialize Rectangle with a given width and height
        Args:
            width (int): Width of the Rectangle
            height (int): Height of the Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of this Rectangle
        Returns:
            int: Width of this Rectangle
        """
        return self.__width

    @property
    def height(self):
        """Retrieve height of Rectangle
        Returns:
            int: Height of Rectangle
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Update the width of Rectangle
        Args:
            value (int): New width of Rectangle
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Update height of Rectangle
        Args:
            value (int): New height of Rectangle
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        '''Compute area of Rectangle
        Returns:
            int: Area of Rectangle
        '''
        return self.width * self.height

    def perimeter(self):
        '''Compute the perimeter of Rectangle
        Returns:
            int: Perimeter of Rectangle
        '''
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)
