#!/usr/bin/python3

from numpy import matmul


def lazy_matrix_mul(m_a, m_b):
    """lazy_matrix_mul multiplies 2 matrices: m_a * m_b"""
    return matmul(m_a, m_b)
