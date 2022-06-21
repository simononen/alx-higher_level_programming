#!/usr/bin/python3
"""Module for working with squares
"""


class Square:
    """Represent a 2D Polygon with 4 equal and perpendicular sides
    """
    def __init__(self, size=0):
        """Initialize square with the given size
        Args:
            size (int): Size of the square
        """
        super().__init__()
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        else:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
