import pandas as pd
from sklearn.linear_model import LinearRegression

x = pd.Series([2.2,4.1,5.5,1.9,3.4,2.6,4.2,3.7,4.9,3.2])
y = pd.Series([71,81,86,72,77,73,80,81,85,74])

X = x.values.reshape(-1, 1) # sklearn は2次元の形を要求
model = LinearRegression().fit(X, y)
print(model.intercept_) # 61.9 ← 切⽚（⼿実装と⼀致！）
print(model.coef_[0]) # 4.52 ← 傾き（⼿実装と⼀致！）

