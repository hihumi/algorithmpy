#!/usr/bin/env python3


"""euclidean_algorithm
"""


def euclidean_algorithm(a, b):
    """euclidean_algorithm
    """

    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b

    print('最大公約数: {}'.format(b))

if __name__ == '__main__':
    a = 221
    b = 143
    euclidean_algorithm(a, b)
