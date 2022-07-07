#!/usr/bin/python3
'''A module for reading a text file (UTF8) and printing0 it to stdout:
'''


def read_file(filename=""):
    '''Reads a file and prints it in standard output.
    Args:
        filename : A given file.
    Returns:
        f : The standard output of the file.
    '''
    with open(filename) as f:
        for line in f:
            print(line, end="")
