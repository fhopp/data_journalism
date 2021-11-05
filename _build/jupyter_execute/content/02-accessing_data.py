#!/usr/bin/env python
# coding: utf-8

# # 2. Accessing Data
# 
# *Damian Trilling and Penny Sheets*
# 
# This notebook is meant to show you different ways of accessing data. Data can be available as (a) local files (on your computer), (b) remote files (somewhere else), or (c) APIs (application programming interfaces). We will show you ways for dealing with all of these.

# But before we do that, we need to import some modules into Jupyter that will help us find and read data.  You already know our basic module, pandas.  Let's import it again just in case your computer cleared it during the break (or in case you're doing this notebook again separately, after class).

# ### Importing Modules
# It is a good custom to import all modules that you need at the beginning of your notebook. We'll explain in the lesson (or in subsequent weeks) what these modules do.

# In[ ]:


import pandas as pd
from pprint import pprint
import json
import matplotlib.pyplot as plt
from collections import Counter
import requests
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# ***

# ## CSV files

# Remember what we did in the first part of class today, working with that Iris dataset? We used pandas to read a CSV file directly from the web and gave its descriptive statistics.

# In[ ]:


iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
iris


# In[ ]:


iris.describe()


# If we want to, we could also plot a histogram:

# In[ ]:


iris.sepal_length.hist()


# Let's say you want to configure that histogram differently, or get axis lables, etc.  Use the help menu to see how to do that:

# In[ ]:


get_ipython().run_line_magic('pinfo', 'iris.sepal_length.hist')


# ## Downloading data
# 
# Probably, if you really want to analyze a dataset, you want to store it locally (=on your computer). Let's download a file with some stock exchange ratings: https://raw.githubusercontent.com/damian0604/bdaca/master/ipynb/stock.csv
# 
# Download it (file-save as or right-clicking) as "all file types" (or .csv); be sure that the extension is correct. Be sure to save it IN THE SAME FOLDER as this jupyter notebook. (Otherwise jupyter won't find it.)

# ## Note!!! Not all CSV files are the same...
# 
# CSV stands for Comma Seperated Value, which indicates that it consists of values (columns) seperated by commas. Just open a CSV file in an editor like Notepad or TextEdit instead of in Excel to understand what we mean.
# 
# Unfortunately, there are many different dialects. For instance, sometimes, a semicolon or a tab is used instead of a comma; sometimes, the first line of a CSV file contains column headers, sometimes not) You can indicate these type of details yourself if pandas doesn't guess correctly.
# 
# Pay special attention when opening a CSV file with Excel: Excel changes the formatting! For instance, it can happen that you open a file that uses commas as seperators in Excel, and when you save it, it suddenly uses semicolons instead. 
# 
# Another reason not to open your files in Excel first: Excel often creates a strange 'encoding' of the characters that causes problems here.  This is why we work just with the raw .csv file if possible.  If you are getting an encoding error, the first step is to re-download the data and do NOT open it in excel (even by mistake, by double-clicking on it).
# 
# 
# We can then open it in the same way as we did before by providing its filename:

# In[ ]:


# stockdata = pd.read_csv('stock.csv') # if you downloaded and saved it locally
stockdata = pd.read_csv('https://raw.githubusercontent.com/damian0604/bdaca/master/ipynb/stock.csv') # when reading directly from source (online)


# Let's have a look...

# In[ ]:


stockdata


# The lefthand column here--called the index--gives you numbers in this case; these are simply the case numbers for each 'row' in the dataset; they may or may not have any meaning on their own, depending on the dataset.  You can also - later in this notebook and later in subsequent weeks - learn how to change these numbers or assign a different column to be the index.

# Because this data seems to be ordered by date in some way, it might be interesting to explore it by making a plot. In this case the plot is different than the histogram; it's not about frequencies of specific values, but rather a plot of all the cases at their value of 'low'.
# 
# We are using a method here called 'plot', provided by pandas.

# In[ ]:


stockdata['Low'].plot()


# ## Trouble with your CSV files?
# For more info on how to format your 'read_csv' commands, or if you're running into problems related to the comma-versus-tab-versus-semicolon issue, look at the help function:

# In[ ]:


get_ipython().run_line_magic('pinfo', 'pd.read_csv')


# ## What if the data isn't in .csv format, but is online? 
#  
#  There is actually a very simple, brilliant, scraping tool that allows you to grab content from tables online and turn that into a csv file.  Then you can use the tools we just used to analyze the csv file (including saving it to your computer and importing it into jupyter for analysis).  The tool is called read_html and allows you to basically put in any website URL and scrape the tables from it.  It probably won't work with all websites (and probably not everything it scrapes is relevant/useful to you), but, it is really handy when it does work.  Let's look, for example, at wikipedia's page involving the premier Dutch football league.
#  
#  First, load the URL into your browswer in another tab to look at the original page.

# In[ ]:


alltables = pd.read_html('https://en.wikipedia.org/wiki/Eredivisie')


# Look at the following code carefully to see what we're doing here. We're introducing a new method ("format") which works for any string; this fills in a value between curly brackets. We also are using function we already know from the first part of today's lesson: "len". 

# In[ ]:


print('We have downloaded {} tables'.format(len(alltables)))


# Here is another, perhaps simpler way to do this, but also less versatile if you want to do fancier stuff someday. 
# 
# **The point here is that there are multiple ways to do many things in python; we just want you to master one way and know why it's useful to you.**

# In[ ]:


print('We have downloaded', len(alltables), 'tables.')


# Let's look at, say, the third table in this set.

# In[ ]:


alltables[2]
#why is this not 3? It is because python uses 0-based indexing, which means that data, values, rows, and items 
#in lists, which you've seen in your coding tutorials, all start at 0. So the first object in a list or index
#is always in position "0", and the second in position "1", and so on.  In this case, to get the 3rd table in
#this new little set of tables, we have to specify "2" rather than "3".


# Now we can save this table to a csv file, which we will call 'test':

# In[ ]:


alltables[2].to_csv('test.csv')


# Now, see if you can go back and read in this test.csv file, have a look at the dataset. 
# 
# If we had more time, we would try to figure out how to rename the columns, and play around with plotting the number of times each team won, for example. (Try this at home, and see if you can do it!  Using the read help command from earlier should help you figure out how to rename columns...or when in doubt, just search online for help!)

# In[ ]:





# In[ ]:





# ## JSON files
# 
# Another type of file we frequently encounter online is the so-called "jason" file - aka, JSON. JSON files allow for nested data structures--like databases.
# 
# JSON is (basically) the same as a collection of Python dicts (dictionaries--we haven't talked about these yet in class, but you did learn about this in your coding tutorials. As a reminder, dicts are collections of key:value pairs, which means you have a category of something (key) and values within it (values)). I'll explain this in class more. Bottom line: it's very easy to look up things by their key, but not by their values. So, knowing our way around these dicts and how they are nested within one another - in a json file - is important.
# 
# Let's download such a file and store it in the same directory as your jupyter notebook.
# Download https://open.data.amsterdam.nl/EtenDrinken.json .
# 
# First, see what happens if you load this link in your browser. You can get a feel for the structure of the dataset, if your browser is relatively fancy.
# 
# 
# Next: we could use pandas to put the JSON file into a table (see next command) -- but as you see, because the data is *nested*, we still have dicts within some of the cells:
# 
# **Note:** The location (often called _path_) where you stored the file is important to remember when you load the data into your notebook. I have saved the json file to a folder called _datasets_, which is located one folder 'above' the current folder where our notebook reside in. So, I have to tell Python to go back one folder ('../'), then into the datasets folder (datasets/), and from there open the file 'EtenDrinken.json'. If you stored the datafile in the same folder as your notebook is in, you can just load it by providing the file name!  
# 
# **Where am I?** If you are unsure where your notebook is running from, simply use the following cell magic to get the path to your current notebook:

# In[ ]:


get_ipython().system('pwd')


# In[ ]:


pd.read_json('../datasets/EtenDrinken.json')
# pd.read_json('EtenDrinken.json') if your file is in the same folder as this notebook


# Sometimes, pandas can be an easy solution for dealing with JSON files, but in this case, it doesn't seem to be the best choice. 
# 
# So, let's read the JSON file into a list of dictionaries instead, since most of these columns seem to include dictionaries. We're going to call it "eat", this new list of dictionaries, because we know from the site this has something to do with eating and drinking.

# In[ ]:


eat = json.load(open('../datasets/EtenDrinken.json'))
#note: nothing happens in terms of output for this command.  
#but now it's in a format we can more easily explore in python.


# ### Playing around with nested JSON data and extracting meaningful information
# 
# NOTE!! You don't need to be able to do all of this already, but it's mostly important that you try to understand the logic behind these various commands. We'll review a lot of this later on when we get to analysis, anyway.

# Let's check what `eat` is and what is in there

# In[ ]:


type(eat)


# In[ ]:


len(eat)


# Maybe let's just look at the *first* restaurant

# In[ ]:


pprint(eat[0])
#pprint stands for 'pretty print'--it's not terribly pretty, 
#but nicer than if you do just a plain old print (try it out!)


# In[ ]:


#do your normal print command here to see the value of pprint.


# We can now directly access the elements we are intereted in:

# In[ ]:


eat[0]['details']['en']['title']


# In[ ]:


eat[0]['location']


# We see that location is itself a dict with a number of key:value pairs. One of these is the zipcode.  So if we want specifically the zipcode for the first restaurant, we have to enter both levels, essentially telling python to call up the first dict, and then look within that one for the second.

# In[ ]:


eat[0]['location']['zipcode']


# Let's say I want to figure out where the most restaurants are, by area, within Amsterdam. But I don't want to do this one-by-one.
# 
# Once we know what we want, we can replace our specific restaurant `eat[0]` by a generic `restaurant` within a *loop*.

# In[ ]:


# let's get all zipcodes
#first, we make a blank list.
zipcodes = []

#then, we make a loop, pulling the zipcode of each restaurant, and add that to the list with "append" as a METHOD.
for restaurant in eat:
    zipcodes.append(restaurant['location']['zipcode'])


# In[ ]:


len(zipcodes)


# What do you think the purpose is of this previous step?
# 
# 
# Next, let's use a counter tool (something we imported above) to count the 20 most frequent zipcodes in this database. You could do 20, or 5, or 10, or 100 - whatever you want.

# In[ ]:


Counter(zipcodes).most_common(20)


# For my little story, however, this data is too specific - the letters at the end of each zipcode make for too detailed a story.  There is a way to cut off the letters and just use the four numbers of each zipcode.  Again, here don't worry about knowing all this code, but, worry about understanding the logic here, and thinking how (eventually) you might want to apply it to your own datasets.

# In[ ]:


zipcodes_without_letters = [z[0:4] for z in zipcodes]
Counter(zipcodes_without_letters).most_common(20)


# ## APIs
# 
# Lastly, we will check out working with a JSON-based API. Some APIs that are very frequently used (e.g., the Twitter API) have an own Python *wrapper*, which means that you can do something like `import twitter` and have some user-friendly commands. Also, many APIs require authentication (i.e., sth like a username and a password).
# 
# We do not want to require all of you to get such an account for the sole purpose of this meeting. We will therefore work with a public API provided by Statistics Netherlands (CBS): https://opendata.cbs.nl/.
# 
# First, we go to https://opendata.cbs.nl/statline/portal.html?_la=en&_catalog=CBS and select a dataset. This kind of website is a great place to explore some potential datasets for your projects.  If you explore a bit, you'll see there are a ton of datasets and a ton of APIs, as well as raw JSON files for you to download and work with.  Take this illustration just as a way to use APIs if the raw data is not also available.
# 
# If there is a specific URL we want to access (like this one we have chosen ahead of time), we can do so as follows:

# In[ ]:


data = requests.get('https://opendata.cbs.nl/ODataApi/odata/37556eng/TypedDataSet').json()


# Let's try some things out to make sense of this data:

# In[ ]:


pd.DataFrame(data)


# What that showed us is that there are 119 rows, with 2 columns.  The first column seems only to be about metadata and URLs, which isn't very interesting.  The second column looks like a series of dicts that might be more interesting for us.  Let's confirm what these two columns are:

# In[ ]:


data.keys()


# Now let's focus only on the 'value' column, and make a new dataframe out of that.

# In[ ]:


df = pd.DataFrame(data['value'])


# In[ ]:


df


# We can actually see that this is a list that works as a 'simple' dataframe--there are rows and columns, and it doesn't look like there is more nested info within here.
# 
# But there are 199 columns!  How can we know what's in this dataset then?  We can create a list using the '.columns' property associated with a dataframe.  This allows us to transform the index into a list to see everything in it:

# In[ ]:


list(df.columns)    


# In[ ]:


#two other ways to tell us ABOUT the columns are this, but these abbreviate the list of columns so we can't read it.
df.columns
df.keys()


# In[ ]:


# So let's choose one column specifically - 'Periods' and figure out more about it.
# What do you think this represents?  What would we need to do to make sense of this/make it useful?
df['Periods']


# In[ ]:


# It would be really nice if our row numbers ('index') wouldn't be a number between 0 and 118, would 
# correspond to this value of 'periods'.  But we need to clean up 'periods' to get just the first four characters
# and to turn those from string (text) values into an integer (number). Here is the command - again, focus on 
# the logic, not the complexity of it.  '.map' is a command, and lamda is a function, and 'x' is an arbitrary label.
df.index = df['Periods'].map(lambda x: int(x[:4]))


# In[ ]:


#Now let's check our work:
df


# In[ ]:


# Now we can plot it, using that same command we used above - plotting a specific value (column) by the index.
# In this case, the index is now the year, which provides a nice little visualization.
df['Marriages_170'].plot()


# ## Play around - and some (non-graded) homework
# 
# The most important thing is that you start playing around. You don't need to be able  to create beautiful plots or anything fancy, but try to get datasets into a usable format and get some insights!
# 
# As an exercise after class, why don't you try the following:
# 
# 1. Find a webpage that has a table on it.
# 2. Use the read_html scraper tool we learned above, to scrape the tables and save these to a csv file.
# 3. Read the csv file back into python, and try to find some basic descriptive statistics (max, min, mean, etc) and if you can, make a simple visualization out of it (histogram or plot).
# 4. Save all of this to a new notebook--code, notes if you have questions or about what you're doing, and output.
# 
# If you can do all of these things, great! If you can't bring your questions to next class.
# 
