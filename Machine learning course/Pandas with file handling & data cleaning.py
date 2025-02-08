#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
# reading the dataset
Titanic = pd.read_excel('Titanic.xlsx')

Titanic.head()


# # handling differnt types of files in pandas 

# In[4]:


# view the first few rows of the dataframe

print("First few rows of the dataframe : ")
print(Titanic.head())


# In[6]:


# view last records

Titanic.tail()


# In[7]:


Titanic.tail(10)


# In[8]:


#  Data types

Titanic.dtypes


# In[9]:


# get a concise summary of daraframe
print("Summary of the DataFrame : ")
Titanic.info()



# In[10]:


# get basic statistics of numerical columns : 
print("basic statistics of numerical columns : ")

Titanic.describe()


# In[12]:


# Titanic.describe(include='all')


# In[13]:


# find missinf values

print("Missing values in each column : ")
Titanic.isnull().sum()

# sum() is defined to check any null values are present or not in the dataset and how many null values are present there.


# In[14]:


#  find unique values 

print("find unique values : ")

Titanic['sex'].unique()


# In[16]:


print(Titanic['sex'].unique())


# In[17]:


# getting count 
print("for getting count : ")

Titanic['sex'].value_counts()


# In[19]:


# checking duplicated rows

print("find duplicated values : ")
print(Titanic.duplicated().sum())


# # data cleaning by pandas

# In[21]:


Titanic.isnull().sum()


# In[22]:


# fill missing values with each median of the colunm


Titanic['age'] = Titanic['age'].fillna(Titanic['age'].median())


# In[23]:


print(Titanic.isnull().sum())


# In[24]:


Titanic['fare']=Titanic['fare'].fillna(Titanic['fare'].median())


# In[25]:


Titanic.isnull().sum()


# In[35]:


Titanic['cabin']= Titanic['cabin'].fillna('null')
Titanic['embarked']= Titanic['embarked'].fillna('null')
Titanic['boat']= Titanic['boat'].fillna('null')
Titanic['body']= Titanic['body'].fillna(Titanic['body'].median())
Titanic['home.dest']= Titanic['home.dest'].fillna('null')


# In[36]:


Titanic.isnull().sum()


# In[37]:


# remove duplicate

Titanic.duplicated().sum()



# In[38]:


# remove duplicating
Titanic=Titanic.drop_duplicates()


# In[7]:


Titanic.info()


# In[8]:


Titanic.head()


# In[9]:


# correcting the data type of the survived column

Titanic['survived'] = Titanic['survived'].astype(float)


# In[10]:


Titanic.head()


# In[16]:


Titanic.dtypes


# In[ ]:





# In[13]:


Titanic["survived"] = Titanic['survived'].astype(int)


# In[14]:


Titanic.dtypes


# In[15]:


Titanic=Titanic[Titanic['survived']>=0]


# In[17]:


# view cleaned data
Titanic


# In[ ]:




