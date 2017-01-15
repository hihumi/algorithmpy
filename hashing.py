#!/usr/bin/env python3


"""hashing
"""


def d_l1():
    d_l = [12, 25, 36, 20, 30, 8, 42]
    return d_l

def h_l1():
    h_l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    return h_l

def hash_func():
    """hash func
    """

    d_l2 = d_l1()
    h_l2 = h_l1()

    k = 0
    i = 0

    while i < len(d_l2):
        k = d_l2[i] % len(h_l2)
        while h_l2[k] != 0:
            k = (k + 1) % len(h_l2)
        h_l2[k] = d_l2[i]
        i += 1

    return h_l2

def hash_method(search_num):
    """hash method
    """

    h_l3 = hash_func()

    k = search_num % len(h_l3)

    while h_l3[k] != 0:
        h_l3[k] == search_num
        try:
            print('find it: index: {}'.format(h_l3.index(search_num)))
            break
        except (IndexError, ValueError):
            print('not foud...')
            break
        k = (k + 1) % len(h_l3)
    else:
        print('not found...')

if __name__ == '__main__':
    d_l1()
    h_l1()
    hash_func()

    search_num = 12
    hash_method(search_num)
