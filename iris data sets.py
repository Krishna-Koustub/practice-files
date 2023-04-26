import pandas as pd
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", names = [' sepal length ','sepal width','petal length','petal width','class'])
print(df.head())
print(df.tail())
