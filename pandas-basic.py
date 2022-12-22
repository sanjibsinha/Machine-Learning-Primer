#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/sanjibsinha/Machine-Learning-Primer/main/Mental%20health%20Depression%20disorder%20Data.csv')
df.head()


# In[4]:


column = df.iloc[:100, df.columns.get_loc('Anxiety disorders (%)')]
column


# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')
column.plot(kind='bar')


# In[ ]:




