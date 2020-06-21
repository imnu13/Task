#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import pandas liabrary.
import pandas as pd


# In[2]:


#importing dataset.
df_Dataset = pd.read_csv('Desktop/Dummy_data.csv')


# In[3]:


df_Dataset.head()


# In[6]:


#to check data types of all variables in dataset.
df = pd.DataFrame(df_Dataset)


# In[7]:


#print data types.
print (df.dtypes)


# In[ ]:




