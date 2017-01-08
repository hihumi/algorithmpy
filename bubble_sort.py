#!/usr/bin/env python3

"""bubble sort
"""

def bubble_sort(data):
    """bubble_sort
    """

    d_l = data

    k = 0
    while k < len(d_l) - 1:
        i = len(d_l) - 1
        while i > k:
            if d_l[i - 1] > d_l[i]:
                w = d_l[i - 1]
                d_l[i - 1] = d_l[i]
                d_l[i] = w
            i -= 1
        k += 1
    print(d_l)

if __name__ == '__main__':
    data1 = [5, 3, 4, 1, 2]
    bubble_sort(data1)

    data2 = [1, 3, 2, 5, 4]
    bubble_sort(data2)
