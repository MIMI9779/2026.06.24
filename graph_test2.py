import pandas as pd
import seaborn as sns # グラフ（簡単・きれい）
import matplotlib.pyplot as plt

x = pd.Series([2.2,4.1,5.5,1.9,3.4,2.6,4.2,3.7,4.9,3.2])
y = pd.Series([71,81,86,72,77,73,80,81,85,74])
xbar, ybar = x.mean(), y.mean()
Sxy = ((x - xbar) * (y - ybar)).sum() # 偏差積和
Sxx = ((x - xbar) ** 2).sum() # x の平⽅和
b1 = Sxy / Sxx # 傾き = 4.52
b0 = ybar - b1 * xbar # 切⽚ = 61.9


print(b1)
print(b0)


