#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Write a Python program to print a dictionary whose keys should be the alphabet from a-z 
#and the value should be corresponding ASCII values
# Create the dictionary
mini_dict = {}
 
for i in range(97, 122):

    mini_dict[chr(i)] = i

print(mini_dict)


# In[47]:


# Python program to create a list of tuples
# from given list having number and
# its cube in each tuple
  

l1 = [1,2,3,4,5]

res = [(val, pow(val, 2)) for val in l1]

print(res)
    
 

