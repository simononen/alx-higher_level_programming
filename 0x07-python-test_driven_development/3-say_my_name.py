#!/usr/bin/python3
'''
say_my_name function
'''


def say_my_name(first_name, last_name=""):
    '''Print first and last name
    Args:
        first_name (str): First Name
        last_name (str): Last Name
    Raises:
        TypeError: If first_name and last_name are not strings
    '''
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    elif not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    else:
        print('My name is {} {}'.format(first_name, last_name))

