# coding=utf8
from sklearn import preprocessing

''' one hot encoding
enc = preprocessing.OneHotEncoder()
enc.fit([[0, 0, 3], [1, 1, 0], [0, 2, 1], [1, 0, 2]])
# dim 1: 0_10,1_01
# dim 2: 0_100,1_010,2_001
# dim 3: 0_1000,1_0100,2_0010,3_0001
# res: 10 010 0001
print(enc.transform([[0, 1, 3]]).toarray())
'''

