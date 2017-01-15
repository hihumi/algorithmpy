#!/usr/bin/env python3


"""sieve_of_eratosthenes
"""


def sieve_of_eratosthenes(data):
    """sieve_of_eratosthenes
    """

    d_l = data

    k = 2
    while k * k <= 100:
        i = k
        while i <= 100 // k:
            d_l[k * i] = 0
            i += 1
        k += 1
        d_l[k] == 0

    i = 2
    while i <= 100:
        if d_l[i] == 1:
            print('{}, '.format(res), end='')
        i += 1
    print()

if __name__ == '__main__':
    data1 = [1 for _ in range(101)]
    print(len(data1))
    sieve_of_eratosthenes(data1)
