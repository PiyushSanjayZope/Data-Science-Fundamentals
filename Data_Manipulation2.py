# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 01:37:33 2021

@author: Dell
"""

import pandas as pd

data = pd.read_csv('vehicles.csv')

data.columns
data2 = data.head(100)

data2.rename(index= str, columns={'url' : 'new_url'}, inplace= True)

#single column
data['region']

#row selection
data[0:100]

#multiple columns
url_city_price = data[['id', 'url', 'region']]
url_city_price2 = data.loc[0:100, ['id', 'url', 'region']]
url_city_price3 = data.iloc[0:100, 0:3]


#dropping single column
drop_no_url = data.drop('url' , axis = 1)

data['age'] = 2021 - data['year']    
data['current_year'] = 2021

#filter
data_new_cars = data[(data.age <= 10)]
data_new_cars_price = data[(data.age <= 10) | (data.price > 5000)]   

data.loc[data.age <= 10, :]    

#new feature creation
data['price_per_mile'] = data['price'] /data['odometer']



#apply function
def price2x(x):
    return x*2
data['price2'] = data['price'].apply(price2x)

data.price.head()
data.price2.head()


#lambda function
data['price3'] = data.price.apply(lambda x: x*3)
data.price3.head()

#ternary operator & numeric to category conversion

data['isexpensive'] = data.price.apply(lambda x: 'expensive' if x > 10000 else 'chep')
data.isexpensive.head(100)
data.isexpensive.head(100).value_counts()


#multiple columns
data['new_and_cheap'] = data.apply(lambda x: 'yes' \
                                   if x['price'] < 10000 \
                                   and x['age'] < 10 else 'no', axis = 1)
data['new_and_cheap'].head(100).value_counts()


#quantiles and bins
data['price_quantiles'] = pd.qcut(data.price, 5)
data['price_quantiles'].value_counts()
pd.cut(data.price, 5).value_counts()


#dummy variables
dummie_vars = pd.get_dummies(data[['price','year','fuel','transmission','type']].head(1000))

#pivote tables
pd.pivot_table(data, index = 'year', columns ='type', \
                 values = 'price', aggfunc = 'mean')
pd.pivot_table(data, index = 'year', columns ='type', \
                 values = 'price', aggfunc = 'mean').sort_index(ascending= False)
pd.pivot_table(data, index = 'year', columns ='type', \
                 values = 'price', aggfunc = 'mean').sort_index(ascending= False).plot()
pd.pivot_table(data, index = 'year', columns ='type', \
                 values = 'price', aggfunc = 'mean').sort_index(ascending= False)
    
pd.pivot_table(data, index = 'year', columns ='type', \
                 values = 'price', aggfunc = 'count').sort_index(ascending= False)
    
    
#group by
groupd_data = data.groupby(['type','year'], as_index = False).mean()

#pd.merge == sql join

df1 = data[['url', 'region']]
df2 = data[['url', 'price']]

df_joined = pd.merge(df1,df2, on = 'url')

#appending

sampl1 = data.sample(100, random_state = 1)
sampl2 = data.sample(100, random_state = 2)

sampl1.append(sampl2)

#write to csv
data.head(1000).to_csv('top_1000.csv') 
