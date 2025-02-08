#!/usr/bin/env python
# coding: utf-8

# # creating plots using seaborn

# In[1]:


# importing imp libraries

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')


# In[2]:


df = pd.read_csv('sample_data.csv')
df.head()


# In[3]:


# set the style for plots
sns.set (style='whitegrid') # use a white grid style for better visulization


# In[7]:


plt.figure(figsize=(6,4))
sns.histplot(df['spending_score'],bins=20, kde=True, color='purple')#histogram with KDE overlay
plt.title('Distribution of spending score')
plt.xlabel('spending score')
plt.ylabel('frequency')
plt.show()


# In[9]:


# 2. scatter plot with hue

plt.figure(figsize=(6,4))
sns.scatterplot(x='income', y='spending_score', data=df, hue='gender', palette='deep',alpha=0.7)
plt.title('income vs spending score')
plt.xlabel('Income')
plt.ylabel('spending score')
plt.show()


# In[10]:


# 3.box plot

plt.figure(figsize=(6,4))
sns.boxplot(x='region', y='income', data=df, palette='pastel') #box plot showing income distribution
plt.title('income distribution')
plt.xlabel('region')
plt.ylabel('income')
plt.show()


# In[11]:


#  4. bar plot


plt.figure(figsize=(6,4))
sns.barplot(x='educational_level', y='income', data=df, palette='muted', estimator='mean') #box plot showing income distribution
plt.title('avg income by education level')
plt.xlabel('education level')
plt.ylabel('avg income')
plt.xticks(rotation=45)
plt.show()


# In[5]:


# 5. pair plot

plt.figure(figsize=(6,4))
sns.pairplot(df[['age','income','spending_score','height','weight','gender']],diag_kind ='kde', hue='gender')
plt.show()


# In[7]:


# 6. heat map (correlation matrix)

plt.figure(figsize=(6,4))
corr_matrix = df[['age','income','spending_score','height','weight']].corr() #compute the correlation matrix
sns.heatmap(corr_matrix, annot =True, cmap='coolwarm', fmt='.2f')
plt.title('correlation heatmap')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




