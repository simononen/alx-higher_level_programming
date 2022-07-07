#!/usr/bin/python3
'''A module that uses json to convert a list to a string:
'''


def to_json_string(my_obj):
    '''Reads a file and prints it in standard output.
    Args:
        my_obj : A python value that would be converted to strings.
    Returns:
        str: A JSON representation of the object if possible,
        otherwise an exception is thrown.
    '''
    import json
    x = json.dumps(my_obj)
    return x
