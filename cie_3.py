# -*- coding: utf-8 -*-
"""CIE-3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1p0tAOKrMJxjkw_jhgKzXXuiDHS1dgTpz
"""

#load the dataset
import pandas as pd
df=pd.read_csv("/content/HousingData.csv")
df.head()

#define the exploratary
df.head()

df.info()

df.describe()

df.duplicated().sum()

df['AGE'].unique()

#perform the preprocessing
null_ZN=df['ZN'].isnull().sum()
null_NOX=df['NOX'].isnull().sum()
mean_ZN=df['ZN'].mean()
mean_NOX=df['NOX'].mean()
df['ZN'].fillna(mean_ZN,inplace=True)
df['NOX'].fillna(mean_NOX,inplace=True)
null_ZN_after=df['ZN'].isnull().sum()
null_NOX_after=df['NOX'].isnull().sum()
print(f"null values in ZN column before:{null_ZN}")
print(f"null values in NOX column after:{null_NOX}")
print(f"null values in ZN column before:{null_ZN}")
print(f"null values in NOX column after:{null_NOX}")

#spliting the data
import pandas as pd
from sklearn.model_selection import train_test_split
x=df['AGE']
y=df['ZN']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
print(x_train)
print(x_test)
print(y_train)
print(y_test)

#load dataset
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
iris=load_iris
df.head()

df.head()

df.info()

df.describe()

df['PetalLengthCm'].unique()

df.duplicated().sum()

#perform the preprocessing
null_PetalLengthCm=df['PetalLengthCm'].isnull().sum()
null_SepalLengthCm=df['SepalLengthCm'].isnull().sum()
mean_PetalLengthCm=df['PetalLengthCm'].mean()
mean_SepalLengthCm=df['SepalLengthCm'].mean()
df['PetalLengthCm'].fillna(mean_ZN,inplace=True)
df['SepalLengthCm'].fillna(mean_NOX,inplace=True)
null_ZN_after=df['PetalLengthCm'].isnull().sum()
null_SepalLengthCm_after=df['SepalLengthCm'].isnull().sum()
print(f"null values in ZN column before:{null_PetalLengthCm}")
print(f"null values in NOX column after:{null_SepalLengthCm}")
print(f"null values in ZN column before:{null_PetalLengthCm}")
print(f"null values in NOX column after:{null_SepalLengthCm}")

#spliting the data
import pandas as pd
from sklearn.model_selection import train_test_split
x=df['PetalLengthCm']
y=df['SepalLengthCm']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
print(x_train)
print(x_test)
print(y_train)
print(y_test)

from sklearn.metrics import mean_squared_error,r2_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
model=LinearRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
mse=mean
r2=r2_score(y_test,y_pred)