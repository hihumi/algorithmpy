#!/usr/bin/env python3


"""binary search
"""


def binary_search(search_num, *args):
    """binary search

    引数:
        *args 探索したい数値(list)

    返り値, 戻り値:
        明示的にはなし

    例:
        data1 = [11, 13, 17, 19, 23, 29, 31]
        binary_search(data1)

    単体テスト: doctest:
    >>> data = [11, 13, 17, 19, 23, 29, 31]
    >>> binary_search(17, data)
    find it: index: 2
    """

    try:
        data_l = list(*args)

        head = 0
        tail = len(data_l) + 1
        center = 0

        while head <= tail:
            center = (head + tail) // 2
            if data_l[center] == search_num:
                print('find it: index: {}'.format(data_l.index(search_num)))
                break
            elif data_l[center] < search_num:
                head = center + 1
            else:
                tail = center - 1
        else:
            print('not found...')

    except (TypeError, ValueError, ZeroDivisionError) as err:
        print('Error: {}'.format(err))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print()

    data = [11, 13, 17, 19, 23, 29, 31]
    binary_search(17, data)
