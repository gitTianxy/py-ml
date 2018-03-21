# coding=utf8
"""
decision tree
---
"""
from io import StringIO
import pandas as pd
import math

data_str = '''
编号,色泽,根蒂,敲声,纹理,脐部,触感,密度,含糖率,好瓜
1,青绿,蜷缩,浊响,清晰,凹陷,硬滑,0.697,0.46,是
2,乌黑,蜷缩,沉闷,清晰,凹陷,硬滑,0.774,0.376,是
3,乌黑,蜷缩,浊响,清晰,凹陷,硬滑,0.634,0.264,是
4,青绿,蜷缩,沉闷,清晰,凹陷,硬滑,0.608,0.318,是
5,浅白,蜷缩,浊响,清晰,凹陷,硬滑,0.556,0.215,是
6,青绿,稍蜷,浊响,清晰,稍凹,软粘,0.403,0.237,是
7,乌黑,稍蜷,浊响,稍糊,稍凹,软粘,0.481,0.149,是
8,乌黑,稍蜷,浊响,清晰,稍凹,硬滑,0.437,0.211,是
9,乌黑,稍蜷,沉闷,稍糊,稍凹,硬滑,0.666,0.091,否
10,青绿,硬挺,清脆,清晰,平坦,软粘,0.243,0.267,否
11,浅白,硬挺,清脆,模糊,平坦,硬滑,0.245,0.057,否
12,浅白,蜷缩,浊响,模糊,平坦,软粘,0.343,0.099,否
13,青绿,稍蜷,浊响,稍糊,凹陷,硬滑,0.639,0.161,否
14,浅白,稍蜷,沉闷,稍糊,凹陷,硬滑,0.657,0.198,否
15,乌黑,稍蜷,浊响,清晰,稍凹,软粘,0.36,0.37,否
16,浅白,蜷缩,浊响,模糊,平坦,硬滑,0.593,0.042,否
17,青绿,蜷缩,沉闷,稍糊,稍凹,硬滑,0.719,0.103,否
'''


def read_data(str_content):
    data_io = StringIO(str_content)
    return pd.read_csv(data_io, sep=',')


def ent(D):
    col = D['好瓜']
    c_total = len(col)
    c_good = 0
    c_bad = 0
    for val in col:
        if val == '是':
            c_good += 1
        else:
            c_bad += 1
    res = 0
    if c_good > 0:
        p_good = c_good / c_total
        res -= p_good * math.log(p_good, 2)
    if c_bad > 0:
        p_bad = c_bad / c_total
        res -= p_bad * math.log(p_bad, 2)
    return res


def ents4attr(D, a):
    col = D[a]
    uniqs = col.unique()
    ents = []
    for u in uniqs:
        ent_u = ent(D.loc[col == u])
        p_u = len(col[col == u]) / len(col)
        ents.append(p_u * ent_u)
    return ents
    # return [ent(D.loc[D[a] == u]) for u in uniqs]


def gain(D, a):
    res = ent(D)
    for g in ents4attr(D, a):
        res -= g
    return round(res, 3)


def a_max_gain(gains):
    a_max = None
    for a,g in gains.items():
        print(a, g)


def train_by_gain():
    attrs = ['色泽','根蒂','敲声','纹理','脐部','触感']
    gains = {}
    for a in attrs:
        gains[a] = gain(df, a)
    print(gains)
    a_max_gain(gains)


if __name__ == '__main__':
    df = read_data(data_str)
    train_by_gain()
