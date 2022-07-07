#!/usr/bin/python3
'''A module for reading a text file (UTF8) and apending a text:
'''


def append_write(filename="", text=""):
    '''Reads a file, appends and prints it in standard output.
    Args:
        filename : A given file.
        text : A string of words to be written into a file.
    Returns:
        n : The f.write function of the text lenght.
    '''
    with open(filename, 'a') as f:
        n = f.write(text)
    return n
