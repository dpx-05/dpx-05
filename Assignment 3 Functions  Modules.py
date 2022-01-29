#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Write a Python function to sum all the numbers in a list.
#list=[8, 2, 3, 0, 7]

list=[8, 2, 3, 0, 7]

total = sum(list)   

print("total of all elements in the list = ",total)


# In[5]:


#Write a Python program to reverse a string.


s="1234abcd"
def reverse(string):
    string = string[::-1]
    return string

print (reverse(s))


# In[13]:


#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

S = 'The quick Brow Fox'

lower= 0

upper = 0

for element in S:
    if(element.islower()):
        lower = lower+1
    elif(element.isupper()):
        upper = upper+1

print(lower)

print(upper)


# In[ ]:




