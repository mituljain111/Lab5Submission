#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
train_data = pd.read_csv('train.csv')
train_data


# In[12]:


import matplotlib.pyplot as plt
plt.scatter(train_data['GrLivArea'], train_data['SalePrice'], alpha = 1/5)
plt.xlabel('GrLivArea', size=9)
plt.ylabel('SalePrice', size=9)
plt.show()


# In[ ]:




