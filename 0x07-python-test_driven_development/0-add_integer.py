#!/usr/bin/python3
'''
add_integer function for TDD project
'''


def add_integer(a, b=98):
    '''
    Calculate sum of two integers
    Args:
        a (int):First number
        b (int): Optional Second number
    Return:
        int: Sum of two integers
    '''
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    elif not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    else:
        return int(a) + int(b)
