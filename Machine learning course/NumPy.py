#!/usr/bin/env python
# coding: utf-8

# # NumPy Nd-arrays

# An ndarrays (n-dimensional array)ia a multidimentional container of items of the same type and size .it allows you to perform operations on large datasets.

# In[1]:


import numpy as np

# creating a 1D array
array_1D = np.array([1,2,3,4,5])
print("1D array : ", array_1D)

# creating 2D array
array_2D = np.array([[1,2,3], [4,5,6]])
print("2D array : \n", array_2D)


# In[9]:


# creating 2D arrays using of zeros

zeros_array = np.zeros((3,4))
print("Array of Zeros :\n",zeros_array)


# In[10]:


# creating a 1D array of ones
ones_array =np.ones(5)
print("Array of ones :\n",ones_array)


# In[11]:


# Creating an array with values from 0 to 9
range_array = np.arange(10)
print("Range Array :\n",range_array)


# In[15]:


# Creating evenly space array

linspace_array = np.linspace(0, 3, 6)
print("Linspace Array : ",linspace_array)


# In[16]:


# for checking shape and size of array and aslo find datatype

# shape = (row, columns)
# size = rows * columns
# dtype = check data type of array

print("Shape of array_2D : ",array_2D.shape)
print("Size of array_2D : ",array_2D.size)
print("datatype of array_2D : ",array_2D.dtype)


# # Indexing and slicing

# In[ ]:


Indexing allow you to access and manipulate specific element within nump arrays.


# In[ ]:


import numpy as np


# # 1. indexing

# In[17]:


array_1d= np.array([10,20,30,40,50])

# accesing the third element by indexing
print("element at index 2 : ",array_1d[2])


# In[23]:


# accessing the last element by the negative indexing
print("Last Element : ",array_1d[-1])
print("second-last Element : ",array_1d[-2])


# In[24]:


# creating 2D array

array_2d = np.array([[10,20,30],[40,50,60]])

# accessing element
print("print element at (1,2) : ",array_2d[1,2])


# In[29]:


# accessing row
print("print element of second row : ",array_2d[1])


# In[28]:


# accessing column
# array_2d[:, 2] = here ':' it means all rows 

print("first column : ",array_2d[:, 2])


# In[31]:


# boolean indexing to select elements greater than 30

boolean_index = array_2d[array_2d >20]
print("Element greater than 30 : ", boolean_index)


# In[33]:


# integer array indexing

print("Elements at indices 0 and 2 of the first row = ",array_2d[0, [0,2]])

# array_2d[0, [0,2]] :here [0,[0,2]] it means first 0 is  shows the 0th row and 
# then select that 0th row and go for 2nd index of 0th row.


# # 2.Slicing

# In[35]:


array_1d= np.array([10,20,30,40,50])

# slicing element from 1 to 3 index

print("slicing element from 1 to 3 index : ",array_1d[1:4])

# here you can see 1st index is including and 4th index is excluding


# In[37]:


slice_step_1d = array_1d[0:5:2]
print("sliced 1D array (0:5:2) : ",slice_step_1d)

# [0:5:2] means start from 0 to end with last means 4th index but, we are
# using here 5 because it is excluding and 2 means skipping two position.


# In[39]:


# creating a 2D array
array_2d = np.array([[10,20,30],[40,50,60],[23,45,66]])

# slicing a sub-array from the first two rows and columns

slice_2D= array_2d[:2, :2]
print("slicing a sub-array from the first two rows and columns : ",slice_2D)


# In[40]:


# slicing first two rows

rows_2d = array_2d[:2]
print("first 2 rows : ",rows_2d)


# In[45]:


# slicing the last column
last_column_2d = array_2d[:,-1]

print("last column: ",last_column_2d)


# In[47]:


# slicing 1st column

first_col =array_2d[:,1]
print("slicing 1st column : ",first_col)


# In[48]:


# slicing every other row

step_rows_2d =array_2d[::2]
print("step_rows_2d  : ",step_rows_2d )


# In[50]:


# slicing every other column
step_columns_2d =array_2d[:, ::2]
print("slicing every other column:\n",step_columns_2d)


# In[ ]:





# In[ ]:





# In[ ]:





# In[3]:


a=np.arange(5,15,2)
np.mean(a)


# In[6]:


np.random.randint(0,10,(3,3))


# In[ ]:





# In[ ]:





# In[ ]:




