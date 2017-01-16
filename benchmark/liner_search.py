#!/usr/bin/env python3


"""liner search
"""


def liner_search(search_data, all_data):
    """liner search

    引数:
        search_data: 探索したい数値
        all_data: 探索対象の配列(list)

    返り値, 戻り値:
        return print('found it: {}'.format(x)):
            探索し該当した数値をprintする

        return print("not found: {}".format(not_found)):
            該当なしの場合をprintする
    """

    not_found = -1

    try:
        for x in all_data:
            if x == search_data:
                return print('found it: {}'.format(x))

        return print('not found: {}'.format(not_found))

    except (TypeError, ValueError) as err:
        print('Error: {}'.format(err))

if __name__ == '__main__':
    import timeit

    with open("sample_data.txt", "r") as file:
        random_num1000 = file.readlines()

    data_l = []
    [data_l.append(int(random_num1000[i])) for i in range(1000)]

    liner_search(997, data_l)

    print(timeit.timeit("liner_search",
                        setup="from __main__ import liner_search"))
    print(timeit.repeat("liner_search",
                        setup="from __main__ import liner_search", repeat=3))
