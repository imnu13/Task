#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df_bill = pd.read_csv('Desktop/bill.csv')


# In[3]:


df_bill.head()


# In[4]:


#to check the whole data type of raw data.
df_bill.dtypes


# In[5]:


#define the date column...as i created my dataset.
df_bill['Order_date']= pd.to_datetime(df_bill.Order_date)


# In[6]:


df_bill.head()


# In[7]:


#Usiing these function datset of single column can be  identifies the datatype.
df_bill.Order_date = pd.to_datetime(df_bill.Order_date)


# In[8]:


df_bill.Order_date.head()


# In[9]:


df_bill.Value_recieve_date  = pd.to_datetime(df_bill.Value_recieve_date )


# In[10]:


df_bill.Value_recieve_date.head()


# In[11]:


#filltered datatypes.
df_bill.dtypes


# In[12]:


#diffrence between the 2 dates columns.
df_bill['Difference'] = df_bill['Order_date'].sub(df_bill['Value_recieve_date'], axis=0)   


# In[13]:


df_bill


# In[15]:


#Droping all the columns and kept the newly computed diffrence column.
df_bill.drop(['Name', 'Bill_Value','Address','Order_date','Value_recieve_date'], axis=1, inplace=True)


# In[16]:


df_bill


# In[ ]:




