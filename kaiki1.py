import seaborn as sns
import pandas as pd, numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = sns.load_dataset("penguins").dropna()
x = df["flipper_length_mm"] # 説明変数
y = df["body_mass_g"] # ⽬的変数

X=x.values.reshape(-1, 1)
model = LinearRegression().fit(X, y)
b0=model.intercept_ # 61.9 ← 切⽚（⼿実装と⼀致！）
b1=model.coef_[0] # 4.52 ← 傾き（⼿実装と⼀致！）

xs = np.linspace(x.min(), x.max(), 100)
sns.scatterplot(data=df, x="flipper_length_mm", y="body_mass_g", hue="species",style="species",palette="colorblind")
plt.plot(xs, b0 + b1*xs, label="Regression line",color="black");plt.legend()
plt.title("Task1")
plt.savefig("演習1.png", bbox_inches="tight")

#R**2
R2=model.score(X,y)

#ひれの⻑さ 205mm のペンギンの体重を 予測する
P=model.predict([[205]])

print(R2)
print(P)