#!/usr/bin/env python3

"""my_mean_while
"""

from decimal import Decimal

def my_mean_while(data):
    """my_mean_while
    """

    d_l = data

    i = 0
    my_sum = 0

    while i < len(d_l):
        print('#', d_l[i])
        my_sum += d_l[i]
        i += 1

    my_mean = Decimal(my_sum) / Decimal(len(d_l))
    print(Decimal(round(my_mean, 4)))

if __name__ == '__main__':
    data1 = [50, 80, 70, 90, 60]
    my_mean_while(data1)

    data2 = [50.5, 80.3, 70.1]
    my_mean_while(data2)
