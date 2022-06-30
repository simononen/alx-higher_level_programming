#!/usr/bin/python3
'''
lazy_matrix_mul function
'''
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    '''
    Multiplies 2 matrices
    Args:
        m_a (list): First matrix.
        m_b (list): Second matrix.
    Returns:
        list: A list of lists of the products of the two matrices
    '''
    return np.matmul(m_a, m_b)

