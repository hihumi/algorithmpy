#!/usr/bin/env python3


"""binary search
"""


def binary_search(search_num, all_data):
    """binary search

    引数:
        search_num: 探索対象の数値
        all_data: 探索対象の配列(list)

    返り値, 戻り値:
        明示的にはなし
    """

    try:
        head = 0
        tail = len(all_data) + 1
        center = 0

        while head <= tail:
            center = (head + tail) // 2
            if all_data[center] == search_num:
                print('find it: index: {}'.format(all_data.index(search_num)))
                break
            elif all_data[center] < search_num:
                head = center + 1
            else:
                tail = center - 1
        else:
            print('not found...')

    except (TypeError, ValueError, ZeroDivisionError) as err:
        print('Error: {}'.format(err))

if __name__ == '__main__':
    import timeit

    with open("sample_data2.txt", "r") as file:
        sorted_random_num1000 = file.readlines()

    data_l = []
    [data_l.append(int(sorted_random_num1000[i])) for i in range(1000)]

    binary_search(150, data_l)

    print(timeit.timeit("binary_search",
                        setup="from __main__ import binary_search"))
    print(timeit.repeat("binary_search",
                        setup="from __main__ import binary_search", repeat=3))
