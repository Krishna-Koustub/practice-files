import os
import sys
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

diabetes = pd.read_csv('pima-indians-diabetes.csv')

print(diabetes.shape)

print(diabetes.describe())

print(diabetes.isnull().sum())

print(diabetes.head())

diabetes_1=(diabetes-diabetes.mean())/diabetes.std()
print(diabetes_1.describe())

from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram
from scipy.cluster.hierarchy import cut_tree

plt.figure(figsize=(18,6))
diabetes  =  linkage(diabetes_X,method='complete',metric='euclidean')
dendrogram(diabetes_X_c)
plt.show()
# plots are not being ploted into this need to fix it

plt.figure(figsize=(20,10))
plt.subplot(2,4,1)
sns.boxplot(y = diabetes.No_Times_Pregnant,color='blue')
plt.subplot(2,4,2)
sns.boxplot(y = diabetes.Plasma_Glucose,color='green')
plt.subplot(2,4,3)
sns.boxplot(y = diabetes.Diastolic_BP,color='red')
plt.subplot(2,4,4)
sns.boxplot(y = diabetes.Triceps,color='cyan')
plt.subplot(2,4,5)
sns.boxplot(y = diabetes.Insulin,color='cyan')
plt.subplot(2,4,6)
sns.boxplot(y = diabetes.BMI,color='red')
plt.subplot(2,4,7)
sns.boxplot(y = diabetes.Age,color='green')
plt.subplot(2,4,8)
sns.boxplot(y = diabetes.Diabetes,color='blue')
plt.show()
