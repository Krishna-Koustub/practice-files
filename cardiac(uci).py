import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

heart_disease_data = pd.read_csv("https://raw.githubusercontent.com/trojrobert/Classification-of-heart-disease-uci-data-/master/heart.csv")
print(heart_disease_data.head)

print(heart_disease_data.describe())

print(heart_disease_data.info())

print(heart_disease_data['target'].value_counts())

heart_disease_data.hist(bins=100, figsize=(30,30))
plt.show()

corr_matrix = print(heart_disease_data.corr())
corr_matrix["target"].sort_values(ascending=False)

print(heart_disease_data.columns)

ax =heart_disease_data[heart_disease_data['target'] == 1]['age'].value_counts().sort_index().plot.bar(
    figsize=(15, 6),
    fontsize= 14,
    title="Frequency  vs age of patient with heart disease",
    rot=0)
print(ax.set_title("Frequency  vs age of patient with heart disease", fontsize=20))
print(ax.set_xlabel("age", fontsize=20))
print(ax.set_ylabel("Frequency", fontsize=20))
