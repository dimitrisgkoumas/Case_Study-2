# -*- coding: utf-8 -*-
"""Case_Study#2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1W8BSYu5fxWQk3S9Qc2hBZruNdNcPDmKo
"""

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files
import seaborn as sns

# Commented out IPython magic to ensure Python compatibility.
from google.colab import drive
drive.mount('/gdrive')
# %cd /gdrive

# Load files
train = pd.read_csv('/gdrive/My Drive/Colab Notebooks/casestudy.csv')

train.info()
train.head()

train.describe()

train['net_revenue'].nunique()
train['customer_email'].nunique()
train['year'].nunique()

train.drop(train.columns[0],axis=1,inplace=True)
train.head()

#•	Total revenue for the current year
train.groupby('year')['net_revenue'].sum().reset_index().rename(columns={'net_revenue':'total_revenue'})

#•	New Customer Revenue e.g. new customers not present in previous year only
train2015=train[train['year']==2015]
train2016=train[train['year']==2016]
train2017=train[train['year']==2017]

#2016
train_dif_16_15=train2016[~train2016.customer_email.isin(train2015.customer_email)]
train_dif_16_15.net_revenue.sum()

#2017
train_dif_17_16=train2017[~train2017.customer_email.isin(train2016.customer_email)]
train_dif_17_16.net_revenue.sum()

#•	Existing Customer Growth. To calculate this,
# use the Revenue of existing customers for current year –(minus) Revenue of existing customers from the previous year

#2016
ex_cust_gr_2016_2015=train2016[train2016.customer_email.isin(train2015.customer_email)]['net_revenue'].sum()-train2015[train2015.customer_email.isin(train2016.customer_email)]['net_revenue'].sum()
ex_cust_gr_2016_2015

#2017
ex_cust_gr_2017_2016=train2017[train2017.customer_email.isin(train2016.customer_email)]['net_revenue'].sum()-train2016[train2016.customer_email.isin(train2017.customer_email)]['net_revenue'].sum()
ex_cust_gr_2017_2016

#•	Revenue lost from attrition

#2016
rev_lost_attr_2016_2015=train2015[~train2015.customer_email.isin(train2016.customer_email)]['net_revenue'].sum()
rev_lost_attr_2016_2015

#2017
rev_lost_attr_2017_2016=train2016[~train2016.customer_email.isin(train2017.customer_email)]['net_revenue'].sum()
rev_lost_attr_2017_2016

#•	Existing Customer Revenue Current Year
#ex_cust_2015=-

#2016
ex_cust_2016=train2016[train2016.customer_email.isin(train2015.customer_email)]['net_revenue'].sum()
ex_cust_2016

#2017
ex_cust_2017=train2017[train2017.customer_email.isin(train2016.customer_email)]['net_revenue'].sum() 
ex_cust_2017

#•	Existing Customer Revenue Prior Year
##ex_cust_2015_pr=-
#ex_cust_2016_pr=-

#2017
ex_cust_2017_pr=ex_cust_2016
ex_cust_2017_pr

#	Total Customers Current Year

train2015['customer_email'].count()

train2016['customer_email'].count()

train2017['customer_email'].count()

#•	Total Customers Previous Year
#2016
tot_cust_2016_2015=train2016['customer_email'].count()/train2015['customer_email'].count()
tot_cust_2016_2015

#2017
tot_cust_2017_2016=train2017['customer_email'].count()/train2016['customer_email'].count()
tot_cust_2017_2016

#•	New Customers
#2016
train2016[~train2016.customer_email.isin(train2015.customer_email)]['customer_email']

#2017
train2017[~train2017.customer_email.isin(train2016.customer_email)]['customer_email']

#•	Lost Customers
#2016
train2015[~train2015.customer_email.isin(train2016.customer_email)]['customer_email']

#2017
train2016[~train2016.customer_email.isin(train2017.customer_email)]['customer_email']

#vis1
k=train.groupby('year')['net_revenue'].sum().reset_index().rename(columns={'net_revenue':'total_revenue'})
sns.barplot(x = 'year', y = 'total_revenue',data = k)

#plots

  
# defining labels
customers = ['exist_revenue_2016', 'new_revenue_2016']
  
# portion covered by each label
revenue =[ex_cust_2016,train_dif_16_15.net_revenue.sum()]
  
# color for each label
colors = ['r','g']
  
# plotting the pie chart
plt.pie(revenue, labels = customers, colors=colors, 
        startangle=90, shadow = True,
        radius = 1.2, autopct = '%1.1f%%')
  
# plotting legend
plt.legend()

# defining labels
customers = ['exist_2017_revenue', 'new_2017_revenue']
  
# portion covered by each label
revenue =[ex_cust_2017,train_dif_17_16.net_revenue.sum()]
  
# color for each label
colors = ['r','g']
  
# plotting the pie chart
plt.pie(revenue, labels = customers, colors=colors, 
        startangle=90, shadow = True,
        radius = 1.2, autopct = '%1.1f%%')
  
# plotting legend
plt.legend()

