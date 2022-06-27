
dule to work with Rectangles
"""


class Rectangle:
    """Represent a 2D Polygon with four perpendicular sides
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle with a given width and height
        Args:
            width (int): Width of the Rectangle
            height (int): Height of the Rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of this Rectangle
        Returns:
            int: Width of Rectangle
        """
        return self.__width

    @property
    def height(self):
        """Retrieve the height of this Rectangle
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
        """Updates the height of Rectangle
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
        '''Computes the area of Rectangle
        Returns:
            int: The area of Rectangle
        '''
        return self.width * self.height

    def perimeter(self):
        '''Computes the perimeter of Rectangle
        Returns:
            int: Perimeter of Rectangle
        '''
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        '''Return a string representation of Rectangle
        Returns:
            str: String representation of Rectangle
        '''
        if self.width == 0 or self.height == 0:
            return ''
        else:
            s = str(self.print_symbol)
            w = self.width
            h = self.height
            res = map(lambda x: (s * w) + ('\n' * (x != h - 1)), range(h))
            return ''.join(list(res))

    def __repr__(self):
        '''Return a representation of this Rectangle's initialization
        Returns:
            str: String representation of this Rectangle's initialization
        '''
        return 'Rectangle({:d}, {:d})'.format(self.width, self.height)

    def __del__(self):
        '''Instance of an object is deleted.
        '''
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Return the biggest rectangle based on the area
        Args:
            rect_1 Rectangle: First Rectangle
            rect_2 Rectangle: Second Rectangle
        Returns:
            Rectangle: Biggest rectangle based on the area
        '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        elif rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

