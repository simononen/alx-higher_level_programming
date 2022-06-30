#!/usr/bin/python3
'''
matrix_divided
'''


def matrix_divided(matrix, div):
    '''
    Divide all elements of matrix
    Args:
        matrix (list): Matrix whose elements to be divided
        div (int): Number for divisor
    Returns:
        list: New list with result of dividing each element
        in the matrix by div
    '''
    messages = (
        'matrix must be a matrix (list of lists) of integers/floats',
        'Each row of the matrix must have the same size',
        'div must be a number',
        'division by zero'
    )
    size = [0, 0]
    res = []
    if not isinstance(matrix, list):
        raise TypeError(messages[0])
    size[0] = len(matrix)
    if size[0] == 0:
        raise TypeError(messages[0])
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(messages[0])
        elif len(row) == 0:
            raise TypeError(messages[0])
        else:
            if size[1] == 0:
                size[1] = len(row)
            elif len(row) != size[1]:
                raise TypeError(messages[1])
            for col in row:
                if not isinstance(col, (int, float)):
                    raise TypeError(messages[0])
    if not isinstance(div, (int, float)):
        raise TypeError(messages[2])
    elif div == 0:
        raise ZeroDivisionError(messages[3])
    else:
        for row in matrix:
            res_row = list(map(lambda x: round(x / div, 2), row))
            res.append(res_row)
        return res
