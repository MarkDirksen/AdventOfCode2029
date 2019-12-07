#!/usr/bin/env python
# coding: utf-8

# In[56]:


import os
import numpy as np
import re


# In[126]:


filepath = 'exampledata.txt'
exampledata = []
with open(filepath) as fp:
    line = fp.readline()
    cnt = 1
    while line:
        exampledata.append(line.strip())
        line = fp.readline()
        cnt += 1


# In[127]:


exampledata_array = []
for i in exampledata:
    reg1 = re.search('(.*)\)', i)
    reg2 = re.search('\)(.*)', i)
    obj1 = i[:reg1.start()] + i[reg1.end():]
    obj2 = i[:reg2.start()] + i[reg2.end():]
    exampledata_array.append([obj2,obj1])


# In[128]:


exampledata_array = np.array(exampledata_array)


# In[66]:


filepath = 'data.txt'
data = []
with open(filepath) as fp:
    line = fp.readline()
    cnt = 1
    while line:
        data.append(line.strip())
        line = fp.readline()
        cnt += 1


# In[68]:


data_array = []
for i in data:
    reg1 = re.search('(.*)\)', i)
    reg2 = re.search('\)(.*)', i)
    obj1 = i[:reg1.start()] + i[reg1.end():]
    obj2 = i[:reg2.start()] + i[reg2.end():]
    data_array.append([obj2,obj1])


# In[69]:


data_array = np.array(data_array)


# In[70]:


data_unique = list(set(data_array[:,1]))


# In[72]:


c = 0
for i in data_unique:
    j = i
    while not(j == 'COM'):
        j = data_array[data_array[:,1] == j,0]
        c = c+1


# In[73]:


c


# In[140]:


start = data_array[data_array[:,1] == 'YOU',0]

def GetNeighbors(Node,array):
    A = list(array[array[:,0] == Node,1])
    B = list(array[array[:,1] == Node,0])
    return(A+B)

def GetPath(Node,FromNode,array):
    neighbors = GetNeighbors(Node,array)
    add_neighbors = [i for i in neighbors if not(i == FromNode)]
    
    if 'SAN' in add_neighbors:
        return([Node])
    elif not add_neighbors:
        return([])
    else:
        for i in add_neighbors:
            x = GetPath(i,Node,array)
            if not(not x):
                return(x + [Node])
            


# In[141]:


GetPath(list(exampledata_array[exampledata_array[:,1] == 'YOU',0])[0],'YOU',exampledata_array)


# In[143]:


len(GetPath(list(data_array[data_array[:,1] == 'YOU',0])[0],'YOU',data_array))


# In[125]:


for i in add_neighbors:
    print(i)


# In[100]:


test == 'C'


# In[101]:


test2 = [i for i in test if not(i == 'C')]


# In[102]:


test2


# In[103]:


'E' in test2


# In[106]:


not ['A','B']


# In[ ]:




