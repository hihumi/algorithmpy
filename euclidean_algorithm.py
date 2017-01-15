#!/usr/bin/env python3


def euclidean_algorithm(a, b):
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b

    print('最大公約数: {0}'.format(b))

if __name__ == '__main__':
    a = 221
    b = 143
    euclidean_algorithm(a, b)
