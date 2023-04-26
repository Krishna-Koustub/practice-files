#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


import pandas as pd

# Read the online file by the URL provides above, and assign it to variable "df"
other_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
df = pd.read_csv(other_path, header=None)


# In[3]:


print("The first 5 rows of the dataframe") 
df.head(5)


# In[4]:


print("enter the last 10 rows \n")
df.tail(10)


# In[5]:


headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
print("headers\n", headers)


# In[6]:


df.columns = headers
df.head(10)


# In[9]:


df1 = df.replace('?',np.NAN)


# In[10]:


df=df1.dropna(subset=["price"], axis=0)
df.head(20)


# In[11]:


print(df.columns)


# In[13]:


df.dtypes


# In[14]:


print(df.dtypes)


# In[16]:


df.describe()


# In[18]:


df.describe(include='all')


# In[19]:


df.info()


# In[ ]:




