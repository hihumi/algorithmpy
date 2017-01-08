#!/usr/bin/env python3

"""my_min
"""

def my_min(data):
    """my_min
    """

    d_l = data

    i = 0
    my_min = d_l[0]

    while i < len(d_l):
        if my_min > d_l[i]:
            my_min = d_l[i]
        i += 1

    print(my_min)

if __name__ == '__main__':
    data1 = [50, 80, 80, 90, 90, 100, 1, 2]
    my_min(data1)
