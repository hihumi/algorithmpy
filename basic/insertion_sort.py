#!/usr/bin/env python3


"""insertion_sort
"""


def insertion_sort(data):
    """insertion_sort
    """

    d_l = data

    i = 1
    while i < len(d_l):
        x = d_l[i]
        k = i

        while k > 0 and d_l[k - 1] > x:
            d_l[k] = d_l[k - 1]
            k -= 1

        d_l[k] = x
        i += 1
    print(d_l)

if __name__ == '__main__':
    import timeit

    data1 = [5, 3, 4, 1, 2]
    insertion_sort(data1)
    print()

    data2 = [1.1, 3, 5, 2.2, 4]
    insertion_sort(data2)
    print()

    print(timeit.timeit("insertion_sort", setup="from __main__ import insertion_sort"))
    print(timeit.repeat("insertion_sort", setup="from __main__ import insertion_sort", repeat = 3))
