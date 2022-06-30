#!/usr/bin/python3
'''
print_square function
'''


def print_square(size):
    '''Print a square with '#'
    Args:
        size (int): Size length of the square
    '''
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    else:
        for i in range(size):
            print('{}'.format('#' * size))

