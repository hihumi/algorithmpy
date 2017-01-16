#!/usr/bin/env python3


"""liner search
"""


def liner_search(search_data, *args):
    """liner search

    引数:
        search_data: 検索したい数値
        *data: 検索する配列(list)

    返り値, 戻り値:
        return print('found it: {0}'.format(x)):
            検索し該当した位置をprintする
        return print("not found: {0}".format(not_found)):
            該当なしの場合をprintする

    例: data1 = [101, 4, 2, 22, 5]
        liner_search(2, data1)
        実行結果: found it: 2


    単体テスト: doctest:
    >>> data1 = [101, 4, 2, 22, 5]
    >>> liner_search(2, data1)
    found it: 2

    >>> data2 = [0, 0, 0, 0, 0]
    >>> liner_search(2, data2)
    not found: -1
    """

    data_l = list(*args)

    not_found = -1

    try:
        for x in data_l:
            if x == search_data:
                return print('found it: {}'.format(x))
        else:
            return print("not found: {}".format(not_found))
    except (TypeError, ValueError) as err:
        print('Error: {}'.format(err))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print()

    data1 = [101, 4, 2, 22, 5]
    liner_search(2, data1)
    print()

    data2 = [0, 0, 0, 0, 0]
    liner_search(2, data2)
