#!/usr/bin/env python
# coding: utf-8

# # 4. Python Data Wrangling I
# 
# *Damian Trilling and Penny Sheets*
# 
# This notebook outlines the
# 
# - (3) Enrichment
# - (4) Analysis
# 
# of two CBS datasets. We made a different notebook (`5. Python Data Wrangling II`) that helps you reconstructing how we
# did the 
# 
# - (1) Retrieval
# - (2) Preprocessing
# 
# to construct the files for this examples.
# 

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# Obtain both datasets by either working through Notebook 5. or by downloading both files from here:
# - [population.json](https://github.com/fhopp/data_journalism/blob/master/datasets/population.json)
# - [economy.json](https://github.com/fhopp/data_journalism/blob/master/datasets/economy.json)

# In[2]:


population=pd.read_json('population.json')
economy=pd.read_json('economy.json')


# # Your Task
# 
# - use methods like `.head()`, `.describe()` and/or `.value_counts()` to get a sense of both datasets.
# - what are the common characteristics between the datasets, what are the differences?

# In[3]:


# your code here


# In[4]:


population.head()


# In[5]:


economy.head()


# In[6]:


population['Periods'].value_counts()


# In[7]:


population.describe()


# In[8]:


economy['Regions'].value_counts().sort_index()


# In[ ]:





# In[ ]:





# # Discuss: What type of join?
# Discuss with your neighbor
# - what type of join (inner, outer, left, right) you want; and
# - which column(s) to join on
# 
# Then, create a combined dataframe with a command along the lines of
# 
# ```
# df = population.merge(economy, on='columnname'], how='left/right/inner/outer')
# ```
# or if you have multiple columns to join on:
# ```
# df = population.merge(economy, on=['columnname','columnname'], how='left/right/inner/outer')
# ```
# 
# 

# In[9]:


df = economy.merge(population, on= ['Periods', 'Regions'], how='left')


# In[10]:


df


# Then, give some information about the resulting dataframe.

# In[11]:


# your code here


# In[12]:


df.describe()


# In[13]:


df


# ## Setting an index
# While our columns have a descriptive names (headers), our rows don't right now. They are just numbers. However, we could actually give them *meaningful* names. A nice side-effect is that you will get better plots, with meaningful axis labels later on.

# In[14]:


df.index=df['Periods']


# See the difference?

# In[15]:


df.head()


# ## Analyze the data
# 
# Let's train a bit with  `.groupby()` and `.agg()`.

# In[16]:


df.plot()


# In[17]:


df['GDPVolumeChanges_1'].plot(kind='bar')


# ## Discuss: Why does the above not work?

# OK, got it?
# 
# Let's try this instead:

# In[18]:


df[['GDPVolumeChanges_1','Regions']].groupby(
    'Regions').agg(np.mean).plot(kind='bar')


# In[19]:


df['LiveBornChildren_2'].groupby('Periods').agg(sum).plot()


# ## Discuss: which aggregation function?
# 
# - Why did we choose `np.mean`?
# - What function should we choose for analyzing `df['LiveBornChildren_2']`? Why?
# 
# 

# In[ ]:





# ### Some more example code for plotting, feel free to play around
# 
# Pay attention to what works well and what doesn't, and how you can use
# 
# - groupby and/or
# - subsetting
# 
# to make plots clearer.

# In[20]:


df.groupby('Regions')['LiveBornChildren_2'].plot()
df.groupby('Regions')['GDPVolumeChanges_1'].plot(secondary_y=True)


# In[21]:


df.groupby(df.index)['LiveBornChildren_2'].agg(sum).plot(legend = True)
df.groupby(df.index)['GDPVolumeChanges_1'].agg(np.mean).plot(legend=True, secondary_y=True)


# In[22]:


df.groupby('Regions')['NetMigrationExcludingAdministrative_19'].plot(legend=True, figsize = [10,10] )


# In[23]:


df[df['Regions']=='Flevoland']['NetMigrationExcludingAdministrative_19'].plot(legend=False, figsize = [4,4] )
df[df['Regions']=='Zuid-Holland']['NetMigrationExcludingAdministrative_19'].plot(legend=False )


# In[24]:


df['Regions']=='Flevoland'


# In[25]:


df.groupby(df.index)['NetMigrationExcludingAdministrative_19'].agg(sum).plot(legend = True)
df.groupby(df.index)['GDPVolumeChanges_1'].agg(np.mean).plot(legend=True, secondary_y=True)


# ### Discuss
# I personally find this last plot a pretty cool one. Do you agree?

# In[26]:


df[['NetMigrationExcludingAdministrative_19','GDPVolumeChanges_1']].corr() # we probably should have lagged one of the variables by a year or so for this.


# In[ ]:





# ## Correlational analysis
# 
# We could also look into some bivariate plots.... 

# In[27]:


df.plot(y='LiveBornChildren_2', x='GDPVolumeChanges_1', kind='scatter')


# In[28]:


sns.lmplot(y='LiveBornChildren_2', x='GDPVolumeChanges_1', data=df,
           fit_reg=True, lowess=False, robust=True) 

