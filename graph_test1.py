import pandas as pd # データを表で扱う
import numpy as np # 数値の計算
import seaborn as sns # グラフ（簡単・きれい）
import matplotlib.pyplot as plt

df = sns.load_dataset("penguins").dropna() # 練習⽤データ（pandasの表）
# ⾃分のデータなら: df = pd.read_csv("data.csv")
# 各グラフは plt.savefig("名前.png") で保存。plt.clf() で次へリセット
sns.histplot(data=df, x="bill_length_mm"); plt.savefig("hist.png"); plt.clf()
sns.boxplot(data=df, x="species", y="body_mass_g"); plt.savefig("box.png"); plt.clf()
sns.countplot(data=df, x="species"); plt.savefig("bar.png"); plt.clf()
# 折れ線グラフ（推移）※ penguins でなく説明⽤のダミー
x = np.arange(1, 8) # numpy で数値の並びを作る
plt.plot(x, [12, 15, 14, 18, 22, 25, 28], marker="o")
plt.savefig("line.png"); plt.clf()

# 散布図（2つの数値の関係）
sns.scatterplot(data=df, x="bill_length_mm", y="bill_depth_mm", hue="species")
plt.savefig("scatter.png"); plt.clf()

# ペアプロット（多変数を⼀望）
sns.pairplot(df, hue="species")
plt.savefig("pairplot.png"); plt.clf()

# ヒートマップ（相関を濃淡で）
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.savefig("heatmap.png"); plt.clf()

# ⾊覚に配慮した配⾊ + ⾊と形の両⽅で区別 + 凡例を外に
sns.scatterplot(data=df, x="bill_length_mm", y="bill_depth_mm",
 hue="species", style="species", # style= で形も変える
 palette="colorblind") # ⾊覚に優しい配⾊
plt.legend(bbox_to_anchor=(1.02, 1), loc="upper left") # 凡例を外へ
plt.savefig("scatter_ud.png", bbox_inches="tight") # 凡例ごと保存