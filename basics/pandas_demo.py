# coding=utf8
import pandas as pd
import requests
import io

print(pd.__version__)

url = "https://storage.googleapis.com/mledu-datasets/california_housing_train.csv"
s = requests.get(url).content
california_housing_dataframe = pd.read_csv(io.StringIO(s.decode("utf8")), sep=",")
print(california_housing_dataframe.describe())
