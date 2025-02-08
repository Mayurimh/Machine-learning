#!/usr/bin/env python
# coding: utf-8

# # K-Meam clustering 

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import warnings

warnings.filterwarnings('ignore')


# In[3]:


data =pd.read_csv("Wholesale customers data.csv")

data.head()


# In[5]:


data.describe()


# In[6]:


data.info()


# In[24]:


# stardardizing the data

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# statistics of scaled data
pd.DataFrame(data_scaled).describe()


# In[35]:


# defining the kmeans function with initialization as k-means++
kme = KMeans(n_clusters=2, init='k-means++')

# fitting the k means algorithm on scaled data
kme.fit(data_scaled)

# inertia on the fitted data
kme.inertia_


# In[14]:


# help(KMeans)


# In[23]:


wcss = []
for cluster in range(1,21):
    kmeans = KMeans(n_clusters = cluster, init ='k-means++')
    kmeans.fit(data_scaled)
    wcss.append(kmeans.inertia_)


# In[28]:


pip install --upgrade scikit-learn


# In[29]:


pip install threadpoolctl==3.1.0 


# In[30]:


pip install --upgrade threadpoolctl


# In[34]:





# In[ ]:




