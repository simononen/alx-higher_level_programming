#!/usr/bin/python3
'''A module that uses json to convert a list to a string:
'''


def from_json_string(my_str):
    '''Reads a file and prints it in standard output.
    Args:
        my_str : A python value that would be converted to strings.
    Returns:
        str: A JSON representation of the object if possible,
        otherwise an exception is thrown.
    '''
    import json
    from io import StringIO

    io = StringIO(my_str)
    x = json.load(io)
    return x
