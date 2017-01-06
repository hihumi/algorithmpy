#!/usr/bin/env python3

"""selection sort
"""

def selection_sort(data):
    """selection_sort
    """

    d_l = data
    print('d_l', d_l)
    print('d_l: len', len(d_l))

    i = 0
    while i < len(d_l) - 1:
        index_min = i
        k = i + 1

        while k < len(d_l):
            if d_l[k] < d_l[index_min]:
                index_min = k
            k = k + 1

        w = d_l[i]
        d_l[i] = d_l[index_min]
        d_l[index_min] = w
        i += 1
    print(d_l)

if __name__ == '__main__':
    data1 = [12, 13, 11, 14, 10]
    selection_sort(data1)
    print()

    data2 = [11, 13, 15, 14, 12, 10, 9]
    selection_sort(data2)
