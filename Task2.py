#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


from scipy.stats import pearsonr


# In[24]:


# Import your data into Python 
df_Dataset = pd.read_csv('Desktop/Dummy_data.csv')


# In[25]:


df_Dataset.head()


# In[26]:


# Convert dataframe into series 
list1 = df_Dataset['Salary'] 
list2 = df_Dataset['Year_of_Experience'] 


# In[27]:


# Apply the pearsonr() 
corr, _ = pearsonr(list1, list2) 
print('Pearsons correlation: %.3f' % corr)


# In[31]:


# Create correlation matrix
corr_matrix = df_Dataset.corr().abs()


# In[32]:


corr_matrix


# In[34]:


import numpy as np


# In[35]:


# Select upper triangle of correlation matrix
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool))


# In[36]:


# Find features with correlation greater than 0.85
to_drop = [column for column in upper.columns if any(upper[column] > 0.85)]


# In[38]:


# Drop features 
df_Dataset.drop(to_drop, axis=1, inplace=True)


# In[40]:


corr_matrix


# In[43]:


print(df_Dataset)


# In[ ]:




