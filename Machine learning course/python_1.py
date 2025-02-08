#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello  mayuri")


# In[5]:


#indentation
def greet(name):
    print("hello",name)
    
greet("mayuri")


# In[16]:


#variable

first_name="Marry"
last_name="Jane"
age=21
isStudent=True
charact='A'
percentage=90.8


print(first_name)


# In[14]:


print(type(first_name))


# In[17]:


print(type(first_name))
print(type(last_name))
print(type(age))
print(type(isStudent))
print(type(charact))
print(type(percentage))


# In[20]:


# operator

# arithmetic operator

print("addition of 2+3 : ",2+3)
print("substratction of 3-2 : ",3-2)
print("multiplication of 3 and 2: ",3*2)
print("division of 4 & 1 :",4/1)
print("floor of 7 & 3 : ",7//3)
print("modulo of 5 & 2 : ",5%2)
print("square of 3 & 2 : ",3**2)


# In[1]:


# comparision operator

a=20
b=10

# ==

print(a==b)
    
# !=
print(a!=b)

# > and <
print(a>b)
print(a<b)

# <= and >=

print(a>=b)
print(a<=b)
    


# In[2]:


# logical

a=True
b=False

print(a and b)
print(a or b)
print(not b)


# In[4]:


# assignment operator
a=5
a=a+1
print(a)

a+=2
print(a)

a-=1
print(a)


# # data structure in python

# In[9]:


# create list
empty_list=[]
# fruits list

fruits=["apple", "banana", "mango"]
print(fruits)

numbers=[1,2,3,4,5]
print(numbers)


booleans=[True, False, True]
print(booleans)

mix=["mayuri", 21, 23.8, True]
print(mix)


# In[10]:


# getting items in list
fruits[0]


# In[15]:


# slicing the list

fruits[0:1]


# In[16]:


fruits[0:2]


# In[20]:


# adding new item

# append

fruits.append("Grapes")


# In[21]:


# insert

fruits.insert(2,"orange")
fruits


# In[23]:


# remove
fruits.remove("orange")
fruits


# In[25]:


# pop

fruits.pop()
fruits


# In[26]:


# tuples

# create tuples

mix=("apple", 21, 23.4, True)
mix


# In[27]:


type(mix)


# In[28]:


mix.append(23)
mix


# In[29]:


mix[3]


# In[30]:


mix[0]


# In[32]:


# mix[2]="mayri"


# In[34]:


mix.count(21)


# In[35]:


mix.index("apple")


# In[36]:


# set

mix_Set={1,"apple",21.7}


# In[37]:


mix_Set


# In[38]:


for ele in mix_Set:
    print(ele)


# In[44]:


# dictionaries
employee={
     "name" : "mayuri",
     "age": 30,
     "isStudent": True}
employee


# In[23]:


employee["age"]


# In[46]:


# modify the dictionary
employee['age']=28
employee


# In[47]:


employee.keys()


# In[53]:


employee.values()


# In[49]:


employee.items()


# # conditional statement

# In[2]:


# if statement 

temp=25

if temp>20:
    print("its a warm day..");
print(temp)


# In[4]:


# if-else

temp=20

if temp>20:
    print("It's warm day..")
else:
    print("It's a cold day...")


# In[9]:


# if-else or if-elif

temp = 26

if temp > 30:
    print("It's a hot day")
elif temp > 25:
    print("its a warm day")
else:
    print("its a cold day")


# In[12]:


#  nested if

temp=16
wheather="rainy"

if temp>15:
    if wheather=="sunny":
        print("it's a sunny day and it's warm")
    else:
        print("it's warm day")
else:
    print("it's a not warm day")


# In[13]:


# for loop 

fruits = ['apple', 'mango', 'banana']

for ele in fruits:
    print(ele);


# In[15]:


for ele in fruits:
    print(ele)
    if ele == "mango":
        break


# In[18]:


# printing square of numbers

for i in range(1,11):
    print(i*i)


# In[19]:


course= "python programming"

for letter in course:
    print(letter)


# In[21]:


# nested for loop

clothes= ["shirt", "pants", "kurties"]
sizes = ["small", "medium", "large"]

for cloth in clothes:
    for size in sizes :
        print(size, cloth)


# In[24]:


print("hello".capitalize())


# In[26]:


print("hello".upper())


# In[28]:


print("HELLO".lower())


# In[29]:


def fun(x, y=2):
    return x*y
print(fun(2))


# In[30]:


5//2


# In[37]:


tu=[1,3,4,5,2,3,1,3]
print(tu.sort(3))


# In[ ]:




