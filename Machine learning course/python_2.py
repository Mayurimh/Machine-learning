#!/usr/bin/env python
# coding: utf-8

# In[1]:


# while loop

number = 10

while number > 0:
    print(number)
    number =number-2


# In[ ]:



        


# In[4]:


# break statement

number = 10
while number >0:
    if number ==5:
        break
    print(number)
    number =number-1
        


# # functions 

# In[6]:


# user defined functions 

# create a function

def greet():
    print("hello , welcome to python programming session.")
    
# calling the function

greet()


# In[8]:


#  function with parameters

# multiplication p=of two numbers

def multiply(a,b):
#     print("multiplication is ",a*b)
    return a*b

multiply(4,2)


# In[9]:


multiply(3,6)


# In[12]:


# N arguments

def multiply(*number):
    total=1
    for num in number:
        total*=num
    return total


# calling function

multiply(2,3)


# In[13]:


multiply(2,3,4)


# In[14]:


multiply(1,3,4,2,3)


# # lambda, map, Zip function

# In[15]:


# lambda function

# lambda funtion is anonymous function
# use can implment only one statement
# lambda parameters : expression

square=lambda x: x**2

square(5)


# In[16]:


# zip function

first_name= ["Joy", "Marry", "Bob"]
last_name= ["smith", 'jane', "Smith"]

full_name= list(zip(first_name, last_name))

full_name


# In[17]:


# Map function

def square(x):
    return x**2

number=[1,2,3,4,5]

squared_number= list(map(square, number))
squared_number


# # classes

# 
# clasees are blue print for creating objects in oops. classes allowyou to bundle of data
# and functionality together, making o=it easier to manage and reuse code.
# 
# 

# In[21]:


#  create a class

# __init__(self) is constructor


class Human:
    
    def __init__(self, name, age):
        self.name=name
        self.age=age
    
    def walk(self):
        print(f"{self.name} is walking")
        
    def talk(self):
        print(f"{self.name} is talking")
        



# In[19]:


h1 = Human("mayuri", 21)
h1.walk()


# In[22]:


h2 = Human("chetan", 18)
h2.talk()


# In[ ]:




