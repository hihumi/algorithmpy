#!/usr/bin/env python3

"""算術平均を出力する
"""

def my_mean(*data):
    """算術平均を出力する関数

    引数: 
        *data: 合計する配列(list)

    返り値, 戻り値:
        明示的にはなし

    例:
        data1 = [1, 2, 3, 4, 5]
        my_mean(data1)
        実行結果: 3.0


    単体テスト: doctest
    >>> data1 = [1, 2, 3, 4, 5]
    >>> my_mean(data1)
    3.0

    >>> data2 = [1.1, 2.2, 3.3]
    >>> my_mean(data2)
    2.2

    >>> data3 = [1.1, 2.2, 3.3, 4.4, 5.5]
    >>> my_mean(data3)
    3.3

    >>> data4 = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]
    >>> my_mean(data4)
    5.5
    """

    try:
        data_list = list(*data)
        
        my_sum = 0
        for i in data_list:
            my_sum += i

        res = my_sum / len(data_list)

    except (TypeError, ValueError) as err:
        print('Error: {0}'.format(err))

    else:
        print(round(res, 2))
        

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    data1 = [1, 2, 3, 4, 5]
    my_mean(data1)

    data2 = [1.1, 2.2, 3.3]
    my_mean(data2)

    data3 = [1.1, 2.2, 3.3, 4.4, 5.5]
    my_mean(data3)

    data4 = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]
    my_mean(data4)

