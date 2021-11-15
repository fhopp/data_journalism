#!/usr/bin/env python
# coding: utf-8

# # 5. Python Data Wrangling II
# 
# *Frederic Hopp and Penny Sheets*
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
# - Topics: Net migration *and* live born children (2/20)
# - Sex: only total (1/3)
# - Regions: all provinces (12/1237)
# 
# This should give you 732 rows and result in the file
# 
# `37259eng_UntypedDataSet_15112021_100104.csv`
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
# `82800ENG_UntypedDataSet_15112021_101225.csv`
# 
# Also download the metadata for later reference.
# 

# ## Preprocessing the data
# ### Population data

# In[ ]:


import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


population = pd.read_csv('37259eng_UntypedDataSet_15112021_100104.csv', delimiter=';')


# In[ ]:


population.head()


# We first remove all columns that are not necessary.

# In[ ]:


population['Sex'].value_counts()


# In[ ]:


population.drop(['Sex','ID'], axis = 1, inplace = True)


# In[ ]:


population


# The values of the column Regions contain weird spaces at the end:

# In[ ]:


population.iloc[0,0]


# We are going to remove them:

# In[ ]:


population['Regions'] = population['Regions'].map(lambda x: x.strip())


# By having a look at the metadata (using CTRL-F for looking for PV20), we can find out what the province codes actually mean. Let's recode that by using a dict to map the keys to more meaningful values.

# In[ ]:


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


# In[ ]:


population['Regions'] = population['Regions'].map(provinces)


# In[ ]:


population.head()


# Let's also represent the Period in a better way. It's a string now, and only the first four digits are meaningful. Let's convert these to an integer. Alternatively, we could opt to convert it to a date (a so-called datetime object).

# In[ ]:


population['Periods'] = population['Periods'].map(lambda x: int(x[:4]))


# In[ ]:


population.head()


# Let's save this:

# In[ ]:


population.to_csv('population.csv')
population.to_json('population.json')


# ### Economic data
# 
# We just do exactly the same for our economic dataset

# In[ ]:


economy = pd.read_csv('82800ENG_UntypedDataSet_15112021_101225.csv', delimiter=';')


# In[ ]:


economy


# In[ ]:


# We only downloaded the total, so we can safely delete:
economy['EconomicSectorsSIC2008'].value_counts()


# In[ ]:


economy.drop(['EconomicSectorsSIC2008','ID'], axis = 1, inplace = True)


# In[ ]:


economy['Regions'] = economy['Regions'].map(lambda x: x.strip())
economy['Regions'] = economy['Regions'].map(provinces)


# In[ ]:


economy['Periods'] = economy['Periods'].map(lambda x: int(x[:4]))


# In[ ]:


economy.head()


# In[ ]:


economy.to_csv('economy.csv')
economy.to_json('economy.json')

