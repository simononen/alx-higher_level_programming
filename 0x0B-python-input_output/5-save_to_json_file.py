#!/usr/bin/python3
'''A module that uses json to write an object to a text:
'''


def save_to_json_file(my_obj, filename):
    '''Reads a file and prints it in standard output.
    Args:
        my_str : A python value that would be converted to strings.
    Returns:
        str: A JSON representation of the object if possible,
        otherwise an exception is thrown.
    '''
    import json
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
