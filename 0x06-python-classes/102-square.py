#!/usr/bin/python3
"""Module for working with squares
"""


class Square:
    """Represent a 2D Polygon with four equal and perpendicular sides
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
        """Update the size of this square
        Args:
            value (int): New size of this square
        Raises:
            TypeError: If `value` is not a int
            ValueError: If `value` is not greater than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        else:
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value

    def area(self):
        """Compute Area of this square
        Returns:
            int: Area of this square
        """
        return self.size ** 2

    def __eq__(self, value):
        '''Perform equality comparison check between two square objects
        Returns:
            bool: True if Area of square objects are equal, else False
        '''
        if isinstance(value, Square):
            return self.area() == value.area()
        else:
            return False

    def __ne__(self, value):
        '''Perform non-equal comparison check between two square object
        Returns:
            bool: True if Area of square objects are not equal, else True
        '''
        if isinstance(value, Square):
            return self.area() != value.area()
        else:
            return True

    def __gt__(self, value):
        '''Perform greater-than comparison check between two square objects
        Returns:
            bool: True if Area of left square object is greater than the second, else False
        Raises:
            TypeError: If `value` not square object
        '''
        if isinstance(value, Square):
            return self.area() > value.area()
        else:
            err_msg = "'>' not supported between instances of 'Square' and"
            val_type = str(type(value)).split("'")[1]
            raise TypeError("{} '{}'".format(err_msg, val_type))
            return False

    def __ge__(self, value):
        '''Perform greater-than-or-equal comparison check between
        two square objects
        Returns:
            bool: True if Area of the left square object is
            greater than or equal to the second, else False.
        Raises:
            TypeError: If `value` is not a square object
        '''
        if isinstance(value, Square):
            return self.area() >= value.area()
        else:
            err_msg = "'>=' not supported between instances of 'Square' and"
            val_type = str(type(value)).split("'")[1]
            raise TypeError("{} '{}'".format(err_msg, val_type))
            return False

    def __lt__(self, value):
        '''Perform less-than comparison check between two square objects
        Returns:
            bool: True if Area of the left square object is
            less than the second, otherwise False.
        Raises:
            TypeError: If `value` not square object
        '''
        if isinstance(value, Square):
            return self.area() < value.area()
        else:
            err_msg = "'<' not supported between instances of 'Square' and"
            val_type = str(type(value)).split("'")[1]
            raise TypeError("{} '{}'".format(err_msg, val_type))
            return False

    def __le__(self, value):
        '''Perform less-than-or-equal comparison check between
        two Square objects
        Returns:
            bool: True if the Area of left square object is
            less than or equal to the second, else False
        Raises:
            TypeError: If `value` not square object
        '''
        if isinstance(value, Square):
            return self.area() <= value.area()
        else:
            err_msg = "'<=' not supported between instances of 'Square' and"
            val_type = str(type(value)).split("'")[1]
            raise TypeError("{} '{}'".format(err_msg, val_type))
            return False
