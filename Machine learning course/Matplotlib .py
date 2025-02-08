#!/usr/bin/env python
# coding: utf-8

# # Matplotlib & Seaborn

# matplotlib is a powerful and widely-sed plotting library for python. it provides a varity of tools for creating static, interactive, and animated visulization in python. wheather you are exploring data creating report.

# 

# In[1]:


# importing necessary library

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



# In[6]:


# define data

months = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
sales = np.array([200,220,250,275,300,320,310,295,280,270,260,250])


# In[11]:


# 1. Basic line plot

plt.figure(figsize=(6,4))
plt.plot(months, sales, marker='o', linestyle='-', color='b') #line plot of sales over months
plt.title("Montly Sales Data") # line plot showing sales trends over the year
plt.xlabel('Month') #label to x-axis
plt.ylabel('Sales') #label to y-axis
plt.grid(True) #show grid lines for better readability
plt.show() #display the plot


# In[12]:


# 2. histogram 

# creating a dataset for histogram
np.random.seed(0) #for reproducibility

data = np.random.normal(loc=0, scale=1, size=1000) #generate random data with normal distribution

# creating histogram
plt.hist(data, bins=30, color='purple',edgecolor='black')#histogram
plt.title("random data distribution")
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


# In[18]:


# 3. Scatter plot
# example of data for scatter plot
np.random.seed(0)

x= np.random.rand(50) * 100
# print(x)

y= np.random.rand(50)*100
# print(y)

plt.figure(figsize=(6,4))
plt.scatter(x,y, color='red', alpha=0.7)
plt.title('Random scatter Plot')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.grid(True)
plt.show()


# In[27]:


# 4. bar plot

categories =np.array(['A','B','C','D','E','F'])
values =np.array([10,55,25,40,35,60,])

plt.figure(figsize=(8,5))
plt.bar(categories, values, color=['blue','red','purple','orange','black'])
plt.title('Categories values')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.grid(False)
plt.show()


# In[32]:


# 5.Box plot

np.random.seed(2)
group1 = np.random.normal(loc=0, scale=1, size=100) #data for group 1
group2 = np.random.normal(loc=1, scale=1.5, size=100) #data for group 2

plt.figure(figsize=(8,5))
plt.boxplot([group1, group2], labels=['Group 1', 'Group 2'])
plt.title('Box plot of two groups')
plt.xlabel('Group')
plt.ylabel('Value')
plt.grid(True)
plt.show()


# In[35]:


# 6. HeatMap (correlation matrix)
# create a correlation matrix for demonstration

np.random.seed(3)
data_matrix= np.random.rand(10,10) #random data matrix

plt.figure(figsize =(6,4))
plt.imshow(data_matrix, cmap='coolwarm', interpolation='none')
plt.colorbar(label='Value')
plt.title("Heatmap of random data matrix")
plt.show()


# # Creating subplot

# In[37]:


x =np.linspace(0,10,100)
print(x)


# In[43]:


y1 =np.sin(x) #sine wave
y2 =np.cos(x) #cosine Wave

# create a figure
plt.figure(figsize=(6,2))

# creating 1st subplot :sine wave
plt.subplot(1,2,1) # 1row, 2columns, first plot
plt.plot(x, y1, 'b-') #line plot for sine wave
plt.title('Sine Wave') #title for subplot


# creating 2nd subplot :cosine wave
plt.subplot(1,2,2) #1row, 2columns, second plot
plt.plot(x,y2,'r--')
plt.title('Cosine Wave')

# adjust layout to avoid overlap
plt.tight_layout()

# display
plt.show()




# In[41]:


# used to take help of any function
help(plt.plot)


# In[45]:


help(plt.imshow)


# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




