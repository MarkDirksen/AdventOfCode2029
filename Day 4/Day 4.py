#!/usr/bin/env python
# coding: utf-8

# --- Day 4: Secure Container ---
# You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.
# 
# However, they do remember a few key facts about the password:
# 
# It is a six-digit number.
# The value is within the range given in your puzzle input.
# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
# Other than the range rule, the following are true:
# 
# 111111 meets these criteria (double 11, never decreases).
# 223450 does not meet these criteria (decreasing pair of digits 50).
# 123789 does not meet these criteria (no double).
# How many different passwords within the range given in your puzzle input meet these criteria?
# 
# Your puzzle input is 265275-781584.

# In[17]:


output=[]
for i in range(265275,781584+1):
    number = str(i)
    if ((int(number[0])<=int(number[1]))&(int(number[1])<=int(number[2]))&(int(number[2])<=int(number[3]))&(int(number[3])<=int(number[4]))&(int(number[4])<=int(number[5]))):
        if ((int(number[0])==int(number[1]))|(int(number[1])==int(number[2]))|(int(number[2])==int(number[3]))|(int(number[3])==int(number[4]))|(int(number[4])==int(number[5]))):
            output.append(int(number))


# In[19]:


len(output)


# Part Two ---
# An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.
# 
# Given this additional criterion, but still ignoring the range rule, the following are now true:
# 
# 112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
# 123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
# 111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
# How many different passwords within the range given in your puzzle input meet all of the criteria?

# In[48]:


output2 = []
for i in output:
    number = str(i)
    nr_list = [number[0],number[1],number[2],number[3],number[4],number[5]]
    for j in range(10):
        if(nr_list.count(str(j))==2):
            output2.append(i)
            break


# In[49]:


for i in output:
    if not(i in output2):
        print(i)


# In[50]:


len(output2)


# In[ ]:




