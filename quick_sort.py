#!/usr/bin/env python3

"""
quick_sort
"""

def quick_sort(data, first, last):
    """quick_sort
    """

    x = data[(first + last) // 2]
    i = first
    j = last

    while True:
        while x > data[i]:
            i += 1

        while x < data[j]:
            j -= 1

        if i >= j:
            break

        tmp = data[i]
        data[i] = data[j]
        data[j] = tmp
        i += 1
        j -= 1

    if first < i - 1:
        quick_sort(data, first, i - 1)
    if last > j + 1:
        quick_sort(data, j + 1, last)

    return data

if __name__ == '__main__':
    data1 = [5, 4, 7, 6, 8, 3, 1, 2, 9]
    print(quick_sort(data1, 0, 8))
