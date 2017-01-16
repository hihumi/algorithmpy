#!/usr/bin/env python3


"""sample_data.txt用に0~999までの乱数(整数)を生成する
"""


import random


def my_random_int():
    """0から999までの乱数(整数)を生成する関数
    """

    random.seed(1)

    res = [random.randint(1, 1000) for _ in range(1000)]
    for i in res:
        print(i)
    # 個数確認
    # print(len(res))

if __name__ == '__main__':
    my_random_int()
