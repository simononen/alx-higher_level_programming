#!/usr/bin/python3
"""Module for working with squares
"""


class Square:
    """Represent a 2D Polygon with 4 equal and perpendicular sides
    """
    def __init__(self, size=0):
        """Initialize square with a given size
        Args:
            size (int): Size of the square
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of this square
        Returns:
            int: Size of this square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Update size of this square
        Args
            value (int): New size of this square
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        else:
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value

    def area(self):
        """Compute area of this square
        Returns:
            int: Area of this square
        """
        return self.size ** 2
