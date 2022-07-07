#!/usr/bin/python3
'''A module for reading a text file (UTF8) and printing0 it to stdout:
'''


def write_file(filename="", text=""):
    '''Reads a file and prints it in standard output.
    Args:
        filename : A given file.
        text : A string of words to be written into a file.
    Returns:
        n : The f.write function of the text lenght.
    '''
    with open(filename, 'w') as f:
        n = f.write(text)
    return n
