#!/usr/bin/python3
"""Module for working with squares
"""


class Square:
    """Represent 2D Polygon with 4 equal and perpendicular sides
    """
    def __init__(self, size):
        """Initialize square with a given size
        Args:
            size (int): Size of the square
        """
        super().__init__()
        self.__size = size
