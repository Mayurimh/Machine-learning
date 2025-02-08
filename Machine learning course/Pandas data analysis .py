#!/usr/bin/env python
# coding: utf-8

# # Data Analysis with Pandas

# In this notebook we'll perform basic data joining, grouping, aggregating, and filtering.

# In[3]:


import pandas as pd

Customer_df = pd.read_csv("Customers.csv")
Orders_df = pd.read_csv("Orders.csv")


# In[10]:


Customer_df


# In[13]:


Orders_df


# In[14]:


Orders_df.describe()


# In[15]:


Orders_df.info()


# In[16]:


Customer_df.info()


# In[18]:


Customer_df['cust_id'].value_counts()


# In[19]:


Customer_df['cust_id'].value_counts().sum()


# In[21]:


# finf total numbers of customers who place th orders
Orders_df['cust_id'].nunique()

Merge datasets on the customer id in two tables
# In[4]:


# merge the datasets on 'cust_id'

merged_df = pd.merge(Customer_df, Orders_df, on='cust_id', how='inner')


# In[23]:


# view the first few rows

print("view merged_df : ")
merged_df.head()


# In[24]:


merged_df


# In[26]:


merged_df.duplicated().sum()


# In[27]:


# checking missiing values

merged_df.isnull().sum()


# In[28]:


# get information 
merged_df.info()


# In[31]:


age_summary = merged_df.groupby('age')['product'].sum()


# In[32]:


age_summary


# In[37]:


country_summary = merged_df.groupby('country')['age'].mean()


# In[38]:


country_summary


# In[5]:


country_summary1 = merged_df.groupby('country').agg({'age':'mean'})


# In[6]:


country_summary1


# In[7]:


high_avg_age = country_summary1[country_summary1['age']>26]
high_avg_age


# In[8]:


country_summary1


# # plaotting

# In[10]:


country_summary1['age'].plot(kind ='bar', figsize =(8,4), title ='avg age by country ', color='lightblue')


# In[11]:


country_summary1['age'].plot(kind='bar', figsize= (8,4), title="Average age by country", color='red')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




