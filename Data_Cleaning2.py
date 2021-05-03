# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 17:31:35 2021

@author: Dell
"""

import pandas as pd

data = pd.read_csv('vehicles.csv')

data.columns

data.describe()

#remove duplicates
data.drop_duplicates(inplace = True)

#check for null values / % of null values
data.isnull().any()

data.isnull().sum()/ data.shape[0]

#remove columns over the threshold

thresh = len(data)*.6

data.dropna(thresh = thresh, axis =1).shape
data.dropna(thresh = 21, axis = 0).shape

#imputing null values
data.odometer
data.odometer.fillna(data.odometer.median()).isnull().any()

#convert text to all upper or lower
data.desc.head()
data.desc.head().apply(lambda x: x.lower())
data.desc.head().apply(lambda x: x.upper())

data.desc.astype(str).apply(lambda x: x.lower())
data.dtypes


#to float
data.cylinders.head()
data.cylinders.dtype
data.cylinders.value_counts()
data.cylinders = data.cylinders.apply(lambda x: str(x).lower().replace('cylinders', '').strip())

data.cylinders.value_counts()
data.cylinders = pd.to_numeric(data.cylinders, errors = 'coerce')

data.cylinders.isnull().sum()
data.cylinders.fillna(data.cylinders.mean(), inplace = True)


#visualizations

data.boxplot('odometer')
data.boxplot('price')

data.hist('odometer')




numeric = data._get_numeric_data()

#import modules

from scipy import stats
import numpy as np

data_outliers = data[(data.price < data.price.quantile(.995)) & (data.price > data.price.quantile(.005))]
data_outliers.boxplot('price')
data_outliers.hist('price')


data_outliers2 = data[(data.odometer < data.odometer.quantile(.995)) & (data.odometer > data.odometer.quantile(.005))]
data_outliers2.boxplot('odometer')
data_outliers2.hist('odometer')

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(data.cylinders.values.reshape(-1,1))
scaler.transform(data.cylinders.values.reshape(-1,1))


scaler.fit_transform(data.cylinders.values.reshape(-1,1))




