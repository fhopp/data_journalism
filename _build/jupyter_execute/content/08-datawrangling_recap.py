#!/usr/bin/env python
# coding: utf-8

# # Recap Data Wrangling
# 
# _Penny Sheets and Damian Trilling_
# 
# In this recap notebook, we will exercise with data wrangling techniques, using a table scraping tool that extracts tables (well, tries to) extract tables from PDF.
# 
# Also have a look at this Cheat Sheet, as a nice reminder/guide to data wrangling:
# https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
# 
# 
# **To follow this example, you need to `pip install tabula-py` first!**
# 
# (**Note:** You may have to do this via your terminal window, or "anaconda prompt" on windows machines, not here in Jupyter itself, but for many of you it may work within juptyter using the code below.)
# 
# Also, have a look at this PDF: http://www.ametsoc.net/sotc2017/StateoftheClimate2017_lowres.pdf
# We will try to get the table from page 113 ( Global tropical cyclone counts).

# In[1]:


# import sys
# !{sys.executable} -m pip install tabula-py


# # !!! This is an example of a table that is *really* messed up, but short, so you might just type it over instead. But that's a great way to demonstrate the techniques.

# In[2]:


import tabula
import pandas as pd


# In[3]:


# turns out that what is called p. 113 is actually page 133 
#(b/c the front matter of the book is numbered differently)
#so you can see we will use the tabula.read_pdf command, give the html address, and specify which page to scrape.

#Note: If you're getting a JDK error, then you didn't install the JDK as indicated in the email yesterday. 

dfs = tabula.read_pdf('http://www.ametsoc.net/sotc2017/StateoftheClimate2017_lowres.pdf',  
                     multiple_tables=False, pages=133)


# In[4]:


print(f"We have {len(dfs)} dataframes.")


# In[5]:


# OK, let's get that df from the (short ;-) ) list of dfs:
df = dfs[0]

#if we display the table, we can see it's very messily scraped compared to what it looks like in the pdf.
df
#but don't panic!


# In[6]:


# Let's first get only the rows that really contain data
# We can see that the first row seems to be the headers of the table.  And after row 8, it's text from the pdf.
# Row 8 is the totals, which we don't really want either, because we can calculate those ourselves of course.
# So, we select just rows 1 up through 7 (up to 8), using the 'iloc' method we learned in an earlier notebook.
datarows = df.iloc[1:8]
datarows


# In[ ]:





# In[7]:


# BUT, let's fix the index so that it starts with 0 (important for some stuff later ('concatenating'))
# Remember, python starts things at 0, not at 1. So a range of 7 would give us 0-6 as values:
datarows.index=range(7)
datarows


# **So... pop quiz! What is already correct, and what still needs to be fixed?**

# In[8]:


datarows.iloc[:,0]   # show us all rows, column 0


# In[9]:


'North Atlantic 18 17 10 6'.split(" ")[-4:]


# In[10]:


# We can see that a lot of good data is tucked into the same cell.  It seems to be separated on spaces.
# Let's split the cells on their spaces and retain only the last four values
datarows.iloc[:,0].map(lambda x: x.split()[-4:])


# In[11]:


# ... let's turn this into its own dataframe (instead of just showing it) 
# [for this, we first make it a list of lists]
# (on very old versins of pandas, do list(xxxxx) instead of xxxxxx.to_list()   )
tmpdf1 = pd.DataFrame(datarows.iloc[:,0].map(lambda x: x.split()[-4:]).to_list())
tmpdf1


# In[12]:


# Let's give it better columnnames:
tmpdf1.columns = ['Tropical Depressions', 'Tropical Storms', 'HurricanTropicalCyclon', 'Major HurricanTropicalCyclon']
tmpdf1


# In[13]:


# Let's concatenate (=glue together) with our data frame from above
newdf = pd.concat([datarows,tmpdf1], axis=1)
newdf


# In[14]:


# Let's fix the first namesd
oldcolumnnames = newdf.columns.to_list()    # on very old versins of pandas, do list(newdf.columns) instead
oldcolumnnames[0] = 'Basin'
oldcolumnnames[1] = 'SS Cat5'
oldcolumnnames[2] = 'ACE'
newdf.columns = oldcolumnnames


# In[15]:


# alternative:
# newdf.rename({"tABle 4.2. Global tropical cyclone counts by basin in 2017.":"Basin"})


# In[16]:


newdf


# In[17]:


# fix Basin name - same as above, but we now retain everything UNTIl the last 4 elements, 
# and then join the first elements with a space again
newdf['Basin'] = newdf['Basin'].map(lambda x: " ".join(x.split()[0:-4]))


# In[18]:


newdf


# In[19]:


# Wanna reorder?
cols = newdf.columns.to_list()
neworder = [cols[0], cols[3], cols[4], cols[5], cols[6], cols[1], cols[2]]
reconstructed_table = newdf[neworder]


# In[20]:


reconstructed_table


# In[ ]:




