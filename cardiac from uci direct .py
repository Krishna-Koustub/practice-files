import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

heart_disease_data = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data")
print(heart_disease_data.head)

print(heart_disease_data.describe())

print(heart_disease_data.info())

heart_disease_data.hist(bins=100, figsize=(30,30))
plt.show()

corr_matrix = print(heart_disease_data.corr())
corr_matrix["target"].sort_values(ascending=False)

print(heart_disease_data.columns)

fig, axarr = plt.subplots(1, 2, figsize=(20, 6))

((heart_disease_data[heart_disease_data['target'] == 1]['sex'].value_counts() / len(heart_disease_data[heart_disease_data['target'] == 1])) * 100).plot.bar(
    rot = 0,
    fontsize= 15,
    title='Percentage of Male to Female',
    ax=axarr[0])
axarr[0].set_title('Percentage of Male to Female with heart disease', fontsize=18)
axarr[0].set_xlabel("age", fontsize=18)
axarr[0].set_ylabel("Percentage", fontsize=18)
axarr[0].set_ylim([0,100])




#Plot the frequency of Male to Female with heart disease
heart_disease_data[heart_disease_data['target'] == 1]['sex'].value_counts().plot.bar(
    rot=0,
    fontsize= 15,
    title='Frequency of Male to Female with heart disease',
    ax=axarr[1])
axarr[1].set_title('Frequency of of Male to Female with heart disease', fontsize=18)
axarr[1].set_xlabel("age", fontsize=18)
axarr[1].set_ylabel("frequency", fontsize=18)


eart_disease_data.columns

ax = heart_disease_data[heart_disease_data['target'] == 1]['age'].value_counts().sort_index().plot.bar(
    figsize=(15, 6),
    fontsize= 14,
    title="Frequency  vs age of patient with heart disease",
    rot=0)
ax.set_title("Frequency  vs age of patient with heart disease", fontsize=20)
ax.set_xlabel("age", fontsize=20)
ax.set_ylabel("Frequency", fontsize=20)


ax = ((heart_disease_data[heart_disease_data['target'] == 1]['age'].value_counts() / len(heart_disease_data)) * 100).sort_index().plot.bar(
    figsize=(15, 6),
    fontsize= 14,
    title="Percentage  vs age of patient with heart disease",
    rot=0)
ax.set_title("Percentage of patient with heart disease age", fontsize=20)
ax.set_xlabel("age", fontsize=20)
ax.set_ylabel("Percentage", fontsize=20)
