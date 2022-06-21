#!/usr/bin/python3
'''Module for working with squares
'''


class Square:
    '''Represent a 2D Polygon with 4 equal and perpendicular sides
    '''
    def __init__(self, size=0):
        '''Initialize square with a given size
        Args:
            size (int): Size of the square
        '''
        self.size = size

    @property
    def size(self):
        '''Retrieve the size of Square
        Returns:
            int: Size of this Square
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''Update the size of this Square
        Args:
            value (int): Size of this Square
        '''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        else:
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value

    def area(self):
        '''Compute area of this Square
        Returns:
            int: Area of this Square
        '''
        return self.size ** 2

    def my_print(self):
        '''Prints a 2D table of the '#' symbol and the size of this square
        '''
        if self.size == 0:
            print('')
        else:
            for i in range(self.size):
                print('{}'.format('#' * self.size))
