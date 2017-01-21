#!/usr/bin/env python3


"""sample_data2.txt用に0~9999までの乱数(整数)を1000個、生成する
"""


import random
# from collections import Counter

def my_random_sample_int():
    """0から9999までの乱数(整数)を1000個、生成する関数
    """

    random.seed(1)

    res = random.sample(range(10000), 1000)

    # sortしない場合:
    # for i in res:
    #     print(i)
    #print(len(res))

    for i in sorted(res):
        print(i)
    #print(len(res))

    # sortしない場合:
    # for i in res:
    #     print(i)
    #print(len(res))

    # 重複していないかどうか:
    # s = set()
    # temp = list(set([x for x in res if x in s or s.add(x)]))
    # print(temp)

    # 重複していないかどうか: Counter を使用する場合:
    # c = Counter(res)
    # print(c)
    # for k, v in c.items():
    #     print('{0}: {1}'.format(k, v))

if __name__ == '__main__':
    my_random_sample_int()
