#!/usr/bin/python3
'''
Module for inspecting an object.
'''


def lookup(obj):
    '''
    Find the list of available attributes and methods of an object
    Args:
        obj (any): A given object.
    Returns:
        list: List of available attributes and methods the object has
    '''
    return dir(obj)
