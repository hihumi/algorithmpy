#!/usr/bin/env python3

"""my_max
"""

def my_max(data):
    """my_max
    """

    d_l = data

    i = 0
    my_max = 0
    j = 0
    while i < len(d_l):
        if my_max < d_l[i]:
            my_max = d_l[i]
            print(my_max)
        i += 1

    print(my_max)

if __name__ == '__main__':
    data1 = [50, 80, 80, 90, 90, 100]
    my_max(data1)
