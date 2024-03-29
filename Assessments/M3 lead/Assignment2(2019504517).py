# -*- coding: utf-8 -*-
"""IBMAssignment2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PK7jDL8Fn9S19REo1DkVEw21TN9SwBfM
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

data_file = pd.read_csv("/content/Churn_Modelling.csv")

"""**UNIVARIATE ANALYSIS**"""

data_file[['CreditScore','Age','Tenure','Balance','EstimatedSalary']].describe()

sns.countplot(data_file.Gender)

x.head()

data_file.boxplot(column=['CreditScore'], grid='False', color='blue')
data_file.hist(column=['CreditScore'],grid='False', edgecolor='black')

print(data_file['CreditScore'].mean())
print(data_file['CreditScore'].median())
print(data_file['CreditScore'].std())

data_file['CreditScore'].value_counts()

sns.kdeplot(data_file['CreditScore'])

"""**BIVARIATE ANALYSIS**"""

data_file[['CreditScore','Age','Tenure','Balance','EstimatedSalary']].corr()

sns.scatterplot(data_file.Age,data_file.CreditScore)

data_file.groupby(by='HasCrCard').agg('mean')[['CreditScore','Age','Tenure','Balance','EstimatedSalary']]

sns.countplot(data=data_file,data_file='HasCrCard',hue='Gender')

pd.crosstab(data_file.Gender,data_file.HasCrCard)

"""**MULTIVARIATE ANALYSIS**"""

sns.pairplot(data=data_file[['CreditScore','Age','Tenure','Balance','EstimatedSalary','HasCrCard']],hue='HasCrCard')

"""**DESCRIPTIVE STATISTICS**"""

data_file.sum()

print(data_file.count())

print(data_file.mode())

print(data_file.min())

print(data_file.max())

print(data_file['CreditScore'].abs())

print(data_file['Tenure'].cumsum())

print(data_file['Tenure'].cumprod())

print(data_file['Tenure'].prod())

data_file.describe(include='all')

print(data_file.describe(include='object'))

print(data_file.describe(include='number'))

"""**HANDLE MISSING VALUES**"""

data_file.isnull()

a=pd.isnull(data_file['Tenure'])
print(a)

x=data_file.fillna(0)
y=data_file.fillna(method='pad')
z=data_file.fillna(method='bfill')
print(x,y,z)

"""**HANDLING OUTLIERS**"""

data_file2=data_file
median = data_file2.loc[y['Age']<100, 'Age'].median()
data_file2.loc[y.Age > 50, 'Age'] = np.nandrop()
data_file2.fillna(median,inplace=True)
sns.boxplot(data_file2.Age)

data_file.skew()

data_file3=data_file[data_file.Exited == 1].Tenure
data_file4=data_file[data_file.Exited == 0].Tenure
plt.xlabel("Tenure")
plt.ylabel("Churn Prediction")
plt.hist([data_file3,data_file4])
plt.show()

a=data_file.iloc[:,3:13].values      #Independent Variables
b=data_file.iloc[:,13:14].values   #Dependant Variables

ct=ColumnTransformer([("oh",OneHotEncoder(),[1,2])],remainder="passthrough")
a=ct.fit_transform(a)

data_file["Geography"].unique()

data_file["Gender"].unique()

import joblib
joblib.dump(ct,"churnct.pkl")

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
x_train,x_test,y_train,y_test = train_test_split(a,b,test_size=0.2,random_state=0)

x_train.shape

x_test.shape

sc=StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)
joblib.dump(sc,"churndc.pkl")