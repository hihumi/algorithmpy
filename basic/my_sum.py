#!/usr/bin/env python3


"""合計を出力する
"""


def my_sum(*data):
    """合計を出力する関数

    引数:
        *data: 合計する配列(list)

    返り値, 戻り値:
        明示的にはなし

    例:
        data1 = [1, 2, 3, 4, 5]
        my_sum(data1)
        実行結果: 15


    単体テスト: doctest
    >>> data1 = [1, 2, 3, 4, 5]
    >>> my_sum(data1)
    15

    >>> data2 = [1.1, 2.2, 3.3]
    >>> my_sum(data2)
    6.6
    """

    try:
        data_list = list(*data)
        res = 0
        for i in data_list:
            res += i

    except (TypeError, ValueError) as err:
        print('Error: {}'.format(err))

    else:
        print(res)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    data1 = [1, 2, 3, 4, 5]
    my_sum(data1)

    data2 = [1.1, 2.2, 3.3]
    my_sum(data2)
