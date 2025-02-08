#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

data = {
'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
'Age': [25, 30, 35, 40, 45],
'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}

Data_df = pd.DataFrame(data)

Data_df


# In[16]:


# find avg
average_age = Data_df['Age'].mean()
print(average_age)


# In[3]:





# In[23]:


age_graterthan_30 = Data_df[Data_df['Age']>30]
age_graterthan_30                           


# In[23]:


df=pd.DataFrame({'A':[1,2,3,4],'B':[5,6,7,8]})
print(df.mean())


# In[21]:


import numpy as np 
arr =np.array([[1,2],[3,4],[5,6]])
print(arr[[0,2],1])


# In[8]:


import matplotlib.pyplot as plt

x= [1,2,3,4,5]
y=[2,3,5,7,11]
plt.bar(x,y)
plt.show()


# In[24]:


Data_df['AgeGroup'] = Data_df['Age'].apply(lambda x: 'Senior' if x>=40 else 'Adult')


# In[25]:


Data_df.head()


# In[29]:


avg_age_groupBy = Data_df.groupby('AgeGroup')['Age'].mean()
avg_age_groupBy


# In[ ]:





# In[ ]:




