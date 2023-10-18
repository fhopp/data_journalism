#!/usr/bin/env python
# coding: utf-8

# # 6. Data Aggregation
# 
# ## Example "WOZ-waarde"
# 
# *Damian Trilling and Penny Sheets*
# 
# This week, we will particularly look at techniques for aggregating data and for joining datasets.
# We use data on housing prices from https://data.amsterdam.nl/ .

# As always, we first import some modules we need and load our data file.

# In[ ]:


import pandas as pd
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# Download the datafile here:
# - [wozwaarde.csv]()

# In[ ]:


df = pd.read_csv('wozwaarde.csv', delimiter=';')


# ## Cleaning up and recoding
# When we inspect the data, we see that each "wijk" seems to be represented by a code (a letter plus two numbers). Essentially, the code is the first word of the "wijk" column. Let's put it into a new coloumn.
# 
# The lambda function says: Take each cell, call the value `x`, split `x` into a list of words (we did that in the week on analyzing text), and then return the 0st element. We then put the result into a new column called `code`.
# 

# In[ ]:


df.head()


# In[ ]:


df['code'] = df['wijk'].map(lambda x: x.split()[0])


# If we now inspect the rows closer, we can see that the "wijken" have a letter and a two-digit numerical code, whereas some rows (e.g., row 10) contain information on the "stadsdeel" level, signified by only the letter.
# 
# This tells us something about the data structure.
# 
# It seems problematic that both are in the same tabel, given that the "stadsdeel" rows are essentially contain aggregated data from the "wijken". We could check that, but it seems very reasonable to assume this, based on just looking at the dataframe.
# 
# Probably, it's a good idea to seperate our dataframe into two different dataframes.
# 
# We can do so by just checking the length of the value in the `code` column that we created.

# In[ ]:


df


# In[ ]:


# select only the "stadsdelen" and put them into a new dataframe
stadsdelen = df[df['code'].map(lambda x: len(x)==1)]
stadsdelen['wijk'] = stadsdelen['wijk'].map(lambda x: x[2:])


# Let's read the information which letter is associated with which "stadsdeel" into a dictionary, that we can later use for recoding.

# In[ ]:


stadsdeelcodes = {}
for k, v in stadsdelen[['wijk','code']].to_dict(orient='index').items():
    stadsdeelcodes.update({v['code']: v['wijk']})


# In[ ]:


stadsdeelcodes


# In[ ]:


# put all "wijken" (which have a code that is longer than 1) into a new dataframe, 
# and remove their code (the first 4 characters) from their name
wijken = df[df['code'].map(lambda x: len(x)>1)]
wijken['wijk'] = wijken['wijk'].map(lambda x: x[4:])


# In[ ]:


wijken


# We can now use the dictionry that we made above to automatically code in which stadsdeel a wijk is located (by looking up the first character (i.e., the letter) of their code in the dictionary `stadsdeelcodes` and putting the corresponding value in a new column, `stadsdeel`.

# In[ ]:


wijken['stadsdeel'] = wijken['code'].map(lambda x: stadsdeelcodes[x[:1]])


# In[ ]:


wijken.columns


# In[ ]:


wijken


# ## From wide to long
# If you look at the dataframe `wijken`, you will see that it is structured in a so-called *wide* format. 
# That means that you have multiple measurements of the same thing (the house vlaues) in different columns, depending on in which year it was measured. 
# 
# In other words: there is no column (variable) `year` that would tell you when a measurement has taken place, but this information is essentially encoded in the column names.
# 
# For many analyses, this is quite unfortunate. After all, we cannout do sth like `.groupby('year')` in a dataset that is formatted this way.
# 
# We will therefore transform it into a more tidy format, a *long* format. The `.melt()` method allows us to do so. We need to specify which variables stay the same and identify the cases (`id_vars`), which columns contain the values (`value_vars`), and how the two new variables to store the old column names and the cell entries in (`var_name` and `value_name`).

# In[ ]:


wijken_long = wijken.melt(id_vars=['wijk','stadsdeel'], 
                          value_vars=['2014', '2015', '2016', '2017', '2018'],
                          value_name='woz-waarde',
                          var_name = 'year')


# In[ ]:


wijken_long


# Let's save it for future usage (and for some other notebooks in the next weeks.

# In[ ]:


wijken_long.to_csv('wijken_long.csv')


# ## Some analysis with `.groupby()` and `.agg()`
# 
# Have a look at the slides for more info on `.groupby()` and `.agg()`.

# In[ ]:


#wijken_long.index = pd.DatetimeIndex(wijken_long.year.map(lambda x: "1-1-{}".format(x)))


# In[ ]:


wijken_long.head()


# In[ ]:


wijken_long.groupby('year').agg(np.mean).plot(xticks=[0,1,2,3,4])


# In[ ]:


wijken_long.groupby(['year','stadsdeel']).agg(np.mean).unstack().plot(
    figsize=[10,7], xticks=range(5))


# As also explained on the slides, the `.unstack()` part is needed to flatten the hierarchical index that grouping by *two* variables creates. If we want to read the table, we don't need to unstack it, but we cannot directly plot the stacked table. Try it with and without! 

# In[ ]:


wijken_long.groupby(['year','stadsdeel']).agg(np.mean).unstack()


# In[ ]:


oost = wijken_long[wijken_long['stadsdeel']=='Oost']


# In[ ]:


oost.groupby(['year','wijk']).agg(np.mean).unstack().plot(figsize=[20,15])


# In[ ]:


oost[oost.wijk=='Dapperbuurt']


# In[ ]:


oost[oost.wijk.str.startswith('Indisch')]


# In[ ]:


wijken_long.groupby(['year','stadsdeel'])['woz-waarde'].agg([min,max])


# In[ ]:


print('Difference between most expensive and least expensive buurt within stadsdeel')
wijken_long.groupby(['year','stadsdeel'])['woz-waarde'].agg(lambda x: max(x)-min(x)).unstack().plot()


# In[ ]:


print('Difference between most expensive and least expensive buurt within stadsdeel')
wijken_long[wijken_long['stadsdeel']!= 'Westpoort'].groupby(
    ['year','stadsdeel'])['woz-waarde'].agg(lambda x: max(x)-min(x)).unstack().plot()


# We see that differences within stadsdeel rise.

# # Now it's your turn.
# 
# Think of other aggregations, either with this or with other datasets!
