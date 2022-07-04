#!/usr/bin/python3
'''
Module contains a class with restrictions
'''


class LockedClass:
    '''
	Represent a class with restricted attribute modification.
    '''
    __slots__ = ['first_name']
