#!/usr/bin/python3
# 100-matrix_mul.py
# Brennan D Baraban <375@holbertonschool.com>
""" matrix multiplication function."""


def matrix_mul(m_a, m_b):
    """
        matrix representing the multiplication of m_a by m_b.
    """

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(w, list) for w in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(w, list) for w in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(x, int) or isinstance(x, float))
               for x in [num for w in m_a for num in w]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(x, int) or isinstance(x, float))
               for x in [num for w in m_b for num in w]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(w) == len(m_a[0]) for w in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(w) == len(m_b[0]) for w in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    inv = []
    for r in range(len(m_b[0])):
        new_r = []
        for cc in range(len(m_b)):
            new_r.append(m_b[cc][r])
        inv.append(new_r)

    new_matrix = []
    for w in m_a:
        new_r = []
        for col in inv:
            prod = 0
            for i in range(len(inv[0])):
                prod += w[i] * col[i]
            new_r.append(prod)
        new_matrix.append(new_r)

    return new_matrix
