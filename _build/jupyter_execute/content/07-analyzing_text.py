#!/usr/bin/env python
# coding: utf-8

# # 7. Analyzing Text
# 
# *Damian Trilling and Penny Sheets*
# 
# This notebook is meant to show you some more ways of analyzing data that go beyond methods like `df.describe()` or `Counter()` etc., which we used last week already. In particular, we are going to look into analyzing textual data.
# 
# We will both look at *bottom up* and *top down* approaches.

# ## Download the data
# We will use a dataset by Schumacher et al. (2016). From the abstract:
# > This paper presents EUSpeech, a new dataset of 18,403 speeches from EU leaders (i.e., heads of government in 10 member states, EU commissioners, party leaders in the European Parliament, and ECB and IMF leaders) from 2007 to 2015. These speeches vary in sentiment, topics and ideology, allowing for fine-grained, over-time comparison of representation in the EU. The member states we included are Czech Republic, France, Germany, Greece, Netherlands, Italy, Spain, United Kingdom, Poland and Portugal.
# 
# Schumacher, G, Schoonvelde, M., Dahiya, T., Traber, D, & de Vries, E. (2016): *EUSpeech: a New Dataset of EU Elite Speeches*. [doi:10.7910/DVN/XPCVEI](http://dx.doi.org/10.7910/DVN/XPCVEI)
# 
# Download and unpack the following file:
# ```
# speeches_csv.tar.gz
# ```
# 
# In the .tar.gz file, you find a .zip file.
# 
# See below a screenshot of how this looks like in Lubuntu (double-click on "speeches_csv.zip" in the left window, then the right window will open. Click on "Extract"). On some systems, you need to actually to three steps of uncompressing: double-click on the tar.gz file to make it a .gz file, and double-click on that one to get the zip file, and then the same thing again for the zip file.
# 
# **On Windows, you may need to install a unzip program like [7zip](https://www.7-zip.org/) first **
# 
# 
# **Within that archive, you find a file `Speeches_UK_Cleaned.csv`. That's the one we need -- save it inthe directory in which you save your Jupyter Notebooks!**
# 
# 

# In[ ]:


from IPython.display import Image
Image("https://github.com/damian0604/bdaca/raw/master/ipynb/euspeech_download.png")


# ## Getting started
# It is a good custom to import all modules that you need at the beginning of your notebook. I'll explain in the leson what these models do

# In[ ]:


import pandas as pd
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


# if you need to install wordcloud, you can do it as follows:
# !pip install wordcloud


# In[ ]:


import wordcloud


# ## Data preparation
# 
# First of all, we will read the dataset in a Pandas Dataframe. In this case, it seems that there are no column headers (try to run it without the header-argument to see what happens!)

# In[ ]:


df = pd.read_csv('Speeches_UK_Cleaned.csv', header=None)   # the first line contains already data and not column headers


# In[ ]:


df[33:37]


# In[ ]:


df.shape


# In[ ]:


df.head()


# We now probably got some sense what the columns mean, so let's give them headers!

# In[ ]:


df.columns = ['what','when','country','who','number', 'text', 'text_clean','language']


# In[ ]:


df.head()


# In[ ]:





# ## Bottom-up analysis
# 
# There are several approaches to data analysis: bottom up and top down. With the former, you try to recognize patterns and describe the data; with the latter, you aim at identifying concepts you have defined in advance. Let's start bottom-up.t
# 
# 
# I give some examples in the following lines, *but try out your own stuff!!*

# In[ ]:


df['who'].value_counts()


# Remember that in Python, everything is an object. Therefore, we can *chain* methods and apply the `.plot()` method to the output object of `.value_counts()` if we want to:

# In[ ]:


df['who'].value_counts().plot(kind='bar')


# In[ ]:





# ### Simple bottom-up approaches to text analysis
# 
# Let's get most common words. The command below basically takes all cleaned texts, joins them together with a space between them, and then splits this long string into words.

# In[ ]:


c = Counter(" ".join(df.text_clean).split())


# In[ ]:


c.most_common(20)


# Let's generate a word cloud instead!
# 
# More  examples at https://github.com/amueller/word_cloud

# In[ ]:


mywordcloud = WordCloud(width=800, height=400).generate(" ".join(df.text_clean))
plt.imshow(mywordcloud, interpolation='bilinear')
plt.axis("off")


# In[ ]:


mywordcloud.to_file('mywordcloud.png')


# In[ ]:


get_ipython().run_line_magic('pinfo', 'mywordcloud')


# Let's now see what happens if we only take some of the speeches:

# In[ ]:


allspeechesbycameron = " ".join(df[df['who']=='D. Cameron']['text_clean'])


# In[ ]:


allspeechesbycameron[:100]


# In[ ]:


len(allspeechesbycameron.split())


# In[ ]:


wordcloud = WordCloud(width=800, height=400).generate(allspeechesbycameron)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")


# ## Let's turn it around and look for specific things (top-down)
# 
# Imagine we are interested in references to `terror`. Feel free to choose any other term!
# 
# We can actually use regular expressions (google for it!), so we can use `[tT]error` to allow for both upper and lower case. Or we can say `[tT]erroris[mt]`.
# 
# Let's first look at it and then make a new column with it

# In[ ]:


df['text'].str.count('[tT]error')


# In[ ]:


df['terrorrefs'] = df['text'].str.count('[tT]error')


# In[ ]:


df['terrorrefs'].describe()


# In[ ]:


df['terrorrefs'].idxmax() 


# In[ ]:


df.iloc[687]


# ### Making comparisons
# 
# Of course, it would be cool to get some idea whether this differs between some groups of speeches. For this, we can use subsetting (see last week) and repeat the analysis three times, or we can use `.groupby`:

# In[ ]:


df.groupby('who')['terrorrefs'].describe()


# In[ ]:


df.groupby('who')['terrorrefs'].sum()


# Instead of counting the number of all references to terror, let's count the number of speeches that have at leas tone reference:

# In[ ]:


df['terrorrefsdummy'] = df['terrorrefs']>0
df['terrorrefsdummy'] = df['terrorrefsdummy'].map(int)
df


# In[ ]:





# In[ ]:


df.groupby('who')['terrorrefsdummy'].sum()


# In the following lines, you find a quick preview of what we will do a bit more on Wednesday: joining tables. Remember that the output generated above can be seen as just another object, which we can turn into a dataframe:

# In[ ]:


terrorspeeches = df.groupby('who')['terrorrefsdummy'].sum()
totalspeeches = df['who'].value_counts()


# In[ ]:


df1 = pd.DataFrame(terrorspeeches)
df1


# In[ ]:


df2= pd.DataFrame(totalspeeches)
df2


# In[ ]:


df1.join(df2)


# In[ ]:


df3 = df1.join(df2)
df3.columns = ['speeches about terror','total speeches']


# In[ ]:


df3


# In[ ]:


df3['ratio'] = df3['speeches about terror']/df3['total speeches']


# In[ ]:


df3


# In[ ]:


df3[['speeches about terror', 'total speeches']].plot(kind='bar')


# In[ ]:


df3['ratio'].plot(kind='bar')


# ## Going in-depth
# We created new columns above to indicate whether a speech was about terrorism or not. We can now reuse this to actually read such a speech.

# In[ ]:


df[df['terrorrefsdummy'] == True]['what'].value_counts()


# In[ ]:


df[df['what'] == "PM's speech to the Jamaican Parliament"]


# In[ ]:


df[df['what'] == "PM's speech to the Jamaican Parliament"]['text'].str.cat()


# In[ ]:


df['words'] = df['text'].map(lambda x: len(x.split()))


# In[ ]:


df.plot(x='words', y='number', style='x')


# # (Non-graded) homework
# 
# Download the whole EU Speech dataset (see beginning of the notebook) and analyze one of the sub-datasets that you are interested in.
# 
# Think about both bottom-up and top-down approaches!
