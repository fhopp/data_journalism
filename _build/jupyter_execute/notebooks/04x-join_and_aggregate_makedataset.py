#!/usr/bin/env python
# coding: utf-8

# # Python Data Wrangling (2)
# 
# *Damian Trilling and Penny Sheets*
# 
# This notebook outlines the retrieval and preprocessing steps we did to construct the files for our examples.
# Thus, this notebook contains the steps
# 
# - (1) Retrieval
# - (2) Preprocessing,
# 
# while the other notebook contains the steps
# 
# - (3) Enrichment
# - (4) Analysis
# 
# ## EXTRA: How did we prepare the dataset?

# ### Population data
# 
# Go to
# https://opendata.cbs.nl/statline/portal.html?_la=en&_catalog=CBS&tableId=37259eng&_theme=1066
# 
# Select the following options:
# - Topics: Net migration *and* live born children (2/25)
# - Sex: only total (1/3)
# - Regions: all provinces (12/1225)
# 
# This should give you 1392 rows and result in the file
# 
# `37259eng_UntypedDataSet_20112018_132903.csv`
# 
# Also download the metadata for later reference.
# 
# ### Economic data
# 
# Go to
# https://opendata.cbs.nl/statline/portal.html?_la=en&_catalog=CBS&tableId=82800ENG&_theme=1064
# 
# Select the following options:
# - Topics: GDP (volume change) (1/2)
# - Economic sectors: A-U all economic activities (1/15)
# - Regions: all provinces (12/77)
# 
# This should give you 264 rows and result in the file
# 
# `82800ENG_UntypedDataSet_20112018_133529.csv`
# 
# Also download the metadata for later reference.
# 

# ## Preprocessing the data
# ### Population data

# In[2]:


import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


population = pd.read_csv('37259eng_UntypedDataSet_20112018_132903.csv', delimiter=';')


# In[5]:


population.head()


# We first remove all columns that are not necessary.

# In[7]:


population['Sex'].value_counts()


# In[8]:


population.drop(['Sex','ID'], axis = 1, inplace = True)


# In[9]:


population


# The values of the column Regions contain weird spaces at the end:

# In[10]:


population.iloc[0,0]


# We are going to remove them:

# In[18]:


population['Regions'] = population['Regions'].map(lambda x: x.strip())


# By having a look at the metadata (using CTRL-F for looking for PV20), we can find out what the province codes actually mean. Let's recode that by using a dict to map the keys to more meaningful values.

# In[17]:


provinces = {"PV20":"Groningen",
"PV21":"Friesland",
"PV22":"Drenthe",
"PV23":"Overijssel",
"PV24":"Flevoland",
"PV25":"Gelderland",
"PV26":"Utrecht",
"PV27":"Noord-Holland",
"PV28":"Zuid-Holland",
"PV29":"Zeeland",
"PV30":"Noord-Brabant",
"PV31":"Limburg"}


# In[19]:


population['Regions'] = population['Regions'].map(provinces)


# In[25]:


population.head()


# Let's also represent the Period in a better way. It's a string now, and only the first four digits are meaningful. Let's convert these to an integer. Alternatively, we could opt to convert it to a date (a so-called datetime object).

# In[22]:


population['Periods'] = population['Periods'].map(lambda x: int(x[:4]))


# In[24]:


population.head()


# Let's save this:

# In[27]:


population.to_csv('population.csv')
population.to_json('population.json')


# ### Economic data
# 
# We just do exactly the same for our economic dataset

# In[36]:


economy = pd.read_csv('82800ENG_UntypedDataSet_20112018_133529.csv', delimiter=';')


# In[32]:


economy


# In[38]:


# We only downloaded the total, so we can safely delete:
economy['EconomicSectorsSIC2008'].value_counts()


# In[39]:


economy.drop(['EconomicSectorsSIC2008','ID'], axis = 1, inplace = True)


# In[40]:


economy['Regions'] = economy['Regions'].map(lambda x: x.strip())
economy['Regions'] = economy['Regions'].map(provinces)


# In[43]:


economy['Periods'] = economy['Periods'].map(lambda x: int(x[:4]))


# In[45]:


economy.head()


# In[46]:


economy.to_csv('economy.csv')
economy.to_json('economy.json')

