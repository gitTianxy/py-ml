# coding=utf8
import pandas as pd
import requests
import io

print(pd.__version__)

url = "https://storage.googleapis.com/mledu-datasets/california_housing_train.csv"
s = requests.get(url).content
california_housing_dataframe = pd.read_csv(io.StringIO(s.decode("utf8")), sep=",")
print(california_housing_dataframe.describe())


def dataframe_demo():
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
    data_io = io.StringIO(data_str)
    df = pd.read_csv(data_io, sep=',')
    # shape(row_num, col_num)
    print("shape:", df.shape)
    # get row
    row = df.loc[0]
    print("first row:", row)
    # get column
    col = df['色泽']
    print("column:", col)
    # get element in row or column
    print(row['色泽'])
    print(col[0])
    print(col.unique())
    # get headers
    print(df.columns.values)


if __name__ == '__main__':
    dataframe_demo()
