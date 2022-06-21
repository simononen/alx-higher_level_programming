#!/usr/bin/python3
'''Module for working with squares
'''


class Square:
    '''Represent a 2D Polygon with four equal and perpendicular sides
    '''
    def __init__(self, size=0, position=(0, 0)):
        '''Initialize a square with a given size
        Args:
            size (int): Size of the square
            position (tuple): The position of the square
        '''
        self.size = size
        self.position = position

    @property
    def size(self):
        '''Retrieve the size of this square
        Returns:
            int: Size of this square
        '''
        return self.__size

    @property
    def position(self):
        '''Retrieve the position of this square
        Returns:
            tuple: Position of this square
        '''
        return self.__position

    @size.setter
    def size(self, value):
        '''Update size of this square
        Args:
            value (int): New size of this square
        '''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        else:
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value

    @position.setter
    def position(self, value):
        '''Update the position of square
        Args:
            value (tuple): New position of this square
        '''
        is_invalid_value = True
        error_msg = 'position must be a tuple of 2 positive integers'
        if isinstance(value, tuple):
            if len(value) == 2:
                if isinstance(value[0], int) and isinstance(value[1], int):
                    if value[0] >= 0 and value[1] >= 0:
                        is_invalid_value = False
        if is_invalid_value:
            raise TypeError(error_msg)
        else:
            self.__position = value

    def area(self):
        '''Compute area of this square
        Returns:
            int: Area of this square
        '''
        return self.size ** 2

    def my_print(self):
        '''Print a 2D table of the '#' symbol and the size of this square
        based on the position it has
        '''
        if self.size == 0:
            print('')
        else:
            print('{}'.format('\n' * self.position[1]), end='')
            for i in range(self.size):
                print('{}{}'.format(' ' * self.position[0], '#' * self.size))
