#!/usr/bin/env python
# coding: utf-8

# # Step-1 Importing libraries and read the data

# In[46]:


import pandas as pd
import numpy as np
import datetime
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
matplotlib.style.use('ggplot')
import calendar


# In[24]:


data=pd.read_csv('D:/uber.csv')
data.head()


# Step-2 Cleaning the data

# In[25]:


data.tail()


# In[26]:


data=data[:-1]


# Checking for null values from data.

# In[27]:


data.isnull().sum()


# In[28]:


sns.heatmap(data.isnull(),yticklabels=False,cmap="viridis")


# Drop/remove the null values from the data.

# In[29]:


data=data.dropna()
sns.heatmap(data.isnull(),yticklabels=False,cmap="viridis")


# Step-3 Transforming the data
# 
# Getting an hour, day, days of the week, a month from the date of the trip.

# In[30]:


data['START_DATE*'] = pd.to_datetime(data['START_DATE*'], format="%m/%d/%Y %H:%M")
data['END_DATE*'] = pd.to_datetime(data['END_DATE*'], format="%m/%d/%Y %H:%M")


# In[31]:


hour=[]
day=[]
dayofweek=[]
month=[]
weekday=[]
for x in data['START_DATE*']:
    hour.append(x.hour)
    day.append(x.day)
    dayofweek.append(x.dayofweek)
    month.append(x.month)
    weekday.append(calendar.day_name[dayofweek[-1]])
data['HOUR']=hour
data['DAY']=day
data['DAY_OF_WEEK']=dayofweek
data['MONTH']=month
data['WEEKDAY']=weekday


# Finding traveling time.

# In[32]:


time=[]
data['TRAVELLING_TIME']=data['END_DATE*']-data['START_DATE*']
for i in data['TRAVELLING_TIME']:
    time.append(i.seconds/60)
data['TRAVELLING_TIME']=time
data.head()


# Calculating the average speed of the trip.

# In[33]:


data['TRAVELLING_TIME']=data['TRAVELLING_TIME']/60
data['SPEED']=data['MILES*']/data['TRAVELLING_TIME']
data.head()


# Step-4 Visualizing the data
# 
# Different categories of data. From data, we can see most of the people use UBER for business purposes.

# In[34]:


sns.countplot(x='CATEGORY*',data=data)


# Histogram for miles. Most of people not having a long trip.

# In[35]:


data['MILES*'].plot.hist()


# Trips for purpose. Mostly the purpose of the trip is meeting and meal/entertain.

# In[36]:


data['PURPOSE*'].value_counts().plot(kind='bar',figsize=(10,5),color='blue')


# Trips per hour of the day.

# In[37]:


data['HOUR'].value_counts().plot(kind='bar',figsize=(10,5),color='green')


# Trips per day of a week. The highest number of trip on Friday.

# In[44]:


data['WEEKDAY'].value_counts().plot(kind='bar',color='green')


# Trips per day of the month

# In[39]:


data['DAY'].value_counts().plot(kind='bar',figsize=(15,5),color='green')


# trips per months
# 

# In[41]:


data['MONTH'].value_counts().plot(kind='bar',figsize=(10,5),color='green')


# The starting points of trips. The highest number of people are from Cary who takes the trip

# In[42]:


data['START*'].value_counts().plot(kind='bar',figsize=(25,5),color='red')


# Comparing all the purpose with miles, hour, day of the month, day of the week, month, Travelling time.

# In[43]:


data.groupby('PURPOSE*').mean().plot(kind='bar',figsize=(15,5))


# In[ ]:




