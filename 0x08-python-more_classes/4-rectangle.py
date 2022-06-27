#!/usr/bin/python3
"""
A module to work with Rectangles
"""


class Rectangle:
    """
    Represent a 2D Polygon with four perpendicular sides
    """
    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle with a given width and height
        Args:
            width (int): Width of the rectangle
            height (int): Width of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieve the width of Rectangle
        Returns:
            int: Width of Rectangle
        """
        return self.__width

    @property
    def height(self):
        """
        Retrieve the height of Rectangle
        Returns:
            int: Width of Rectangle
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Update the width of Rectangle
        Args:
            value (int): The new width of Rectangle
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """
        Update the height of Rectangle
        Args:
            value (int): The new height of Rectangle
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        '''
        Compute the area of Rectangle
        Returns:
            int: The area of Rectangle
        '''
        return self.width * self.height

    def perimeter(self):
        '''
        Compute the perimeter of Rectangle
        Returns:
            int: The perimeter of Rectangle
        '''
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        '''
        Return a string representation of Rectangle
        Returns:
            str: String representation of Rectangle
        '''
        if self.width == 0 or self.height == 0:
            return ''
        else:
            res = list(map(
                lambda x: '#' * self.width + '\n' * (x != self.height - 1),
                range(self.height)))
            return ''.join(res)

    def __repr__(self):
        '''
        Return a representation of Rectangle's initialization
        Returns:
            str: String representation of Rectangle's initialization
        '''
        return 'Rectangle({:d}, {:d})'.format(self.width, self.height)

