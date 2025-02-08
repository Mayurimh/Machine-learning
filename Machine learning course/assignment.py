#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Create and use functions and lists in Python

def square(x):
    return x*x

numbers=[1,2,3,4,5,6,7,8]
    
newSquared_List= list(map(square,numbers))

print(newSquared_List)


# In[6]:


squared_list=[]
def square(nums):
    for i in nums:
        squared_list.append(i*i)
    return squared_list
    
        
numbers=[1,2,3,4,5,6,7,8,9,10]
print(numbers)
square(numbers)



# In[44]:


StudentsMarks= {"Joy":78, "Bob":45, "Marry":89, "Smith":49, "Jenny":57}
for i in StudentsMarks:
    print(i)


# In[45]:


students_high_Score=[]
student_name=[]

def Student(Stud_Marks):
    for student in Stud_Marks:
        if Stud_Marks[student]>50:
            students_with_high_Score.append(Stud_Marks[student])
            student_name.append(student)
            
    return dict(zip(student_name, students_with_high_Score))
new=Student(StudentsMarks)
print(new)


# In[55]:


import math
name=["Jenny", "Marry", "Bob", "Joy"]
score=[58,45,66,77]

def Multiply(x):
    return x*1.1

myDict=dict(zip(name,map(Multiply,score)))
myDict


# # numpy assignment

# In[1]:


import numpy as np

rng =np.random.default_rng()

array_1 =rng.integers(1,51, size=12)
print(array_1)


# In[28]:


array = np.arange(1,13)
print(array)


# In[25]:


matrix = array.reshape(4,3)
print(matrix)


# In[5]:


max_value = np.max(matrix)
print("Maximum number : ",max_value)

min_value = np.min(matrix)
print("Minimum number : ",min_value)

mean = np.mean(matrix)
print("Mean of matrix : ",mean)


# In[26]:


second_row = matrix[1]
print(second_row)


# In[27]:


print('2 x 2 matrix :\n',matrix[:2, :2])


# In[ ]:




