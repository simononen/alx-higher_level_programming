#!/usr/bin/python3
"""Module to work with Rectangles
"""


class Rectangle:
    """Represent 2D Polygon with four perpendicular sides
    """
    def __init__(self, width=0, height=0):
        """Initializes a Rectangle with a given width and height
        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of this Rectangle
        Returns:
            int: Width of this Rectangle
        """
        return self.__width

    @property
    def height(self):
        """Retrieve the height of this Rectangle
        Returns:
            int: Height of this Rectangle
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Update the width of this Rectangle
        Args:
            value (int): The new width of this Rectangle
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Update the height of this Rectangle
        Args:
            value (int): The new height of this Rectangle
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        '''Compute the area of this Rectangle
        Returns:
            int: Area of this Rectangle
        '''
        return self.width * self.height

    def perimeter(self):
        '''Compute the perimeter of this Rectangle
        Returns:
            int: Perimeter of this Rectangle
        '''
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        '''Return a string representation of this Rectangle
        Returns:
            str: String representation of this Rectangle
        '''
        if self.width == 0 or self.height == 0:
            return ''
        else:
            res = list(map(
                lambda x: '#' * self.width + '\n' * (x != self.height - 1),
                range(self.height)))
            return ''.join(res)

    def __repr__(self):
        '''Return a representation of this Rectangle's initialization
        Returns:
            str: String representation of this Rectangle's initialization
        '''
        return 'Rectangle({:d}, {:d})'.format(self.width, self.height)

    def __del__(self):
        '''Instance of an object is deleted
        '''
        print('Bye rectangle...')

