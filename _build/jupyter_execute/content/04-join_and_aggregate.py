#!/usr/bin/env python
# coding: utf-8

# # 4. Python Data Wrangling I
# 
# *Frederic Hopp and Penny Sheets*
# 
# This notebook outlines the
# 
# - (3) Enrichment
# - (4) Analysis
# 
# of two CBS datasets. We made a different notebook that helps you to reconstruct how we
# did the 
# 
# - (1) Retrieval
# - (2) Preprocessing
# 
# to construct the files for this examples.

# In[ ]:


import pandas as pd
import numpy as np
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


population=pd.read_json('population.json')
economy=pd.read_json('economy.json')


# # Your Task
# 
# - use methods like `.head()`, `.describe()` and/or `.value_counts()` to get a sense of both datasets.
# - what are the common characteristics between the datasets, what are the differences?

# In[ ]:


# your code here


# In[ ]:


population.head()


# In[ ]:


economy.head()


# In[ ]:


population['Periods'].value_counts()


# In[ ]:


population.describe()


# In[ ]:


economy['Regions'].value_counts().sort_index()


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

# In[ ]:


df = economy.merge(population, on= ['Periods', 'Regions'], how='left')


# In[ ]:


df


# Then, give some information about the resulting dataframe.

# In[ ]:


# your code here


# In[ ]:


df.describe()


# In[ ]:


df


# ## Setting an index
# While our columns have a descriptive names (headers), our rows don't right now. They are just numbers. However, we could actually give them *meaningful* names. A nice side-effect is that you will get better plots, with meaningful axis labels later on.

# In[ ]:


df.index=df['Periods']


# See the difference?

# In[ ]:


df.head()


# ## Analyze the data
# 
# Let's train a bit with  `.groupby()` and `.agg()`.

# In[ ]:


df.plot()


# In[ ]:


df['GDPVolumeChanges_1'].plot(kind='bar')


# ## Discuss: Why does the above not work?

# OK, got it?
# 
# Let's try this instead:

# In[ ]:


df[['GDPVolumeChanges_1','Regions']].groupby(
    'Regions').agg(np.mean).plot(kind='bar')


# In[ ]:


df['LiveBornChildren_3'].groupby('Periods').agg(sum).plot()


# ## Discuss: which aggregation function?
# 
# - Why did we choose `np.mean`?
# - What function should we choose for analyzing `df['LiveBornChildren_3']`? Why?
# 
# 

# ### Some more example code for plotting, feel free to play around
# 
# Pay attention to what works well and what doesn't, and how you can use
# 
# - groupby and/or
# - subsetting
# 
# to make plots clearer.

# In[ ]:


df.groupby('Regions')['LiveBornChildren_3'].plot()
df.groupby('Regions')['GDPVolumeChanges_1'].plot(secondary_y=True)


# In[ ]:


df.groupby(df.index)['LiveBornChildren_3'].agg(sum).plot(legend = True)
df.groupby(df.index)['GDPVolumeChanges_1'].agg(np.mean).plot(legend=True, secondary_y=True)


# In[ ]:


df.groupby('Regions')['NetMigrationIncludingAdministrative_17'].plot(legend=True, figsize = [10,10] )


# In[ ]:


df[df['Regions']=='Flevoland']['NetMigrationIncludingAdministrative_17'].plot(legend=False, figsize = [4,4] )
df[df['Regions']=='Zuid-Holland']['NetMigrationIncludingAdministrative_17'].plot(legend=False )


# In[ ]:


df['Regions']=='Flevoland'


# In[ ]:


df.groupby(df.index)['NetMigrationIncludingAdministrative_17'].agg(sum).plot(legend = True)
df.groupby(df.index)['GDPVolumeChanges_1'].agg(np.mean).plot(legend=True, secondary_y=True)


# ### Discuss
# I personally find this last plot a pretty cool one. Do you agree?

# In[ ]:


df[['NetMigrationIncludingAdministrative_17','GDPVolumeChanges_1']].corr() # we probably should have lagged one of the variables by a year or so for this.


# In[ ]:





# ## Correlational analysis
# 
# We could also look into some bivariate plots.... 

# In[ ]:


df.plot(y='LiveBornChildren_3', x='GDPVolumeChanges_1', kind='scatter')


# In[ ]:


sns.lmplot(y='LiveBornChildren_3', x='GDPVolumeChanges_1', data=df,
           fit_reg=True, lowess=False, robust=True) 

