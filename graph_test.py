import pandas as pd
import seaborn as sns

df = sns.load_dataset("penguins").dropna() # 練習⽤データを表で読み込む
 # .dropna() = ⽋損(空欄)のある⾏を除く
# ⾃分のデータなら: df = pd.read_csv("data.csv")
print(df.head()) # 先頭の数⾏を⾒る
print(df["body_mass_g"].mean()) # 体重の平均を計算
print(df.groupby("species")["body_mass_g"].mean()) # 種ごとの平均