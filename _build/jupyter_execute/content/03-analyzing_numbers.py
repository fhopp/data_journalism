#!/usr/bin/env python
# coding: utf-8

# # 3. Basic Statistics
# 
# *Damian Trilling and Penny Sheets*
# 
# This notebook is designed to show you some ways to use python for basic statistical analysis of numbers, and to explore some methods that go beyond `df.describe()` or `Counter()`, which we used last week. In particular, we are going to look into analyzing numerical data. Next week, we will focus on textual data.
# 
# The dataset we use in this example is a subset of the data presented in Trilling, D. (2013). *Following the news. Patterns of online and offline news use*. PhD thesis, University of Amsterdam. http://hdl.handle.net/11245/1.394551
# 

# ### Import our tools/modules/libraries
# 
# As always, we first import the tools we'll need. Today, we'll use pandas (usually imported as "pd"), and something called statsmodels, and something called numpy. We also use matplotlib for some visualizations. A lot of other stuff here we will need for some specific analyses later on; you don't have to worry about all of it right now.
# 
# If you want to learn more about these modules, you can look online for info.

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import statsmodels as sm
import statsmodels.formula.api as smf
from statsmodels.stats.weightstats import ttest_ind
from scipy.stats import kendalltau
import numpy as np


# ### Read data into a dataframe
# We will read a dataset based on Trilling (2013). It contains some sociodemographic variables as well as the number of days the respondent uses a specific medium to access information about news and current affairs.
# 
# You should download the dataset (with the 'save page as' method, making sure .txt isn't appended to the file extension) into the same folder as this jupyter notebook: https://raw.githubusercontent.com/damian0604/bdaca/master/ipynb/mediause.csv
# 
# Remember that the 'df' here is arbitrary; last week we used the names 'iris' and 'stockdata' and others; this week we're going more basic and just saying 'df' for dataframe.

# In[2]:


# df = pd.read_csv('mediause.csv') # if you downloaded and stored the file locally 
df = pd.read_csv('https://raw.githubusercontent.com/damian0604/bdaca/master/ipynb/mediause.csv') # if directly reading it from source 


# Using the .keys() method is way to find out what the columns are in your dataframe. Sometimes they have nice labels already, and sometimes they don't.  In this case, we're in luck.

# In[3]:


df.keys()


# Remember that for a dataframe or object in python, you can simply type its name in a code cell and python will display it as best it can. (In this case, it works well.) 

# In[4]:


df


# ### Explore the dataset
# Let's do some descriptive statistics, using the .describe() method we saw last week. This would be important if you wanted to describe the dataset to your audience, for example.

# In[5]:


df.describe()


# If you want to find out how many possible values there are for a specific variable, you can use the `.value_counts()` method. In this case, you select the dataframe (which we've called `df`), select the column/variable you want to examine, and then apply the method.
# 
# The output shows us that there are two values - 0 and 1 - for the 'gender' variable. It gives us how many instances (aka frequencies) of each of these values exist in the dataset.

# In[6]:


df['gender'].value_counts()


# In[7]:


#as with any method, value_counts() has parameters we can adjust.
#by default, the results are sorted by size of the count, but we can
#also allow it to be random if we wanted. Compare the results.

df['education'].value_counts(sort=False)


# In[8]:


df['education'].value_counts(sort=True)


# In[9]:


#if it is useful to sort by the index - i.e. days of the week here - then you can specify that as follows:
df['education'].value_counts().sort_index()


# In[10]:


#You can also use a help command to get python to print info about this method. But in this case, 
#you have to make an additional step, because the selected column isn't an object until
#it is officially run in a 'real' command. So you have to turn that into an object, and then ask for help.

test = df['education']
get_ipython().run_line_magic('pinfo', 'test.value_counts')


# You can also display value counts for multiple variables at once, to get an overview of your data.  In this case, use a loop to replicate commands for each of the four media types. We'll do this next, but we'll also set a few specifications so that it prints out nicely. 
# 
# See if you can figure out what each of these print commands is doing.

# In[11]:


for medium in ['radio','newspaper','tv','internet']:
    print(medium.upper())
    print(df[medium].value_counts(sort=True, normalize=True))
    print('-------------------------------------------\n')
    


# So that's one way to start exploring a dataset generally.
# 
# ## Groupby
# 
# Let's say you'd like to compare the media use of men and women in the dataset. Eventually we'll move toward statistical comparison, but for now we can start by looking at their descriptive statistics - separately for men and women.
# 
# In python, this is quite easy, using the `.groupby()` method.
# 
# First, we group the dataframe by the 'gender' variable, and then apply a method to that grouped dataframe; this is called 'chaining' multiple methods together.  (We saw a bit of this chaining idea last week already.)
# 

# In[12]:


df.groupby('gender').describe()


# Sometimes in this case, it's more useful to transpose the dataset, making columns into rows and vice versa.  This display will then be much easier to look at.  In this case, we use a .T at the end, after the describe() method.  This doesn't change the dataframe in any way, just displays it differently for you here.

# In[13]:


df.groupby('gender').describe().T


# In[14]:


#try this again here, using a different variable as the grouping variable.


# In[15]:


#you can use help again here, to figure out all the specifications.

get_ipython().run_line_magic('pinfo', 'df.groupby')


# And, as we did last week, you can plot a simple histogram of the distribution of a variable across the dataset. So if you want to look at how 'radio' (as in, how many days per week a person uses radio) is distributed among your sample, e.g., you can use a histogram.

# In[16]:


#Here, 'bins' refers to how many bars we want, essentially. If you don't specify, python/pandas will guess based
#on the dataset. This can be misleading. So if you know how many you want to display, you should specify.

df['radio'].hist(bins=7)


# In[17]:


#Try to plot a histogram of internet news use here:


# One of the modules we imported above helps us to make prettier plots (but no, it's not called "pretty plot" like "pretty print"). Here we can plot the value counts for internet news use in a bar chart, again sorted by the index.
# 
# In particular, the histogram above is very good for continous variables, that we want to 'bin' into fewer bins (=bars). But if we only have a small number of discrete values (like here: the integers from 0 to 7), then the alignment of the labels above may be more confusing. 
# 
# Let's try to use `.plot()` to make a bar chart:

# In[18]:


df['internet'].value_counts().sort_index().plot(kind='bar')


# ## POP QUIZ!
# 
# Can you integrate this plotting method in your for-loop (from above) to get a nice series of plots?  Fill in the missing line of code, below.  But keep the plt.show() command afterward, in order to display all plots.
# 

# In[19]:


for medium in ['radio','newspaper','tv','internet']:
    print(medium.upper())
    print(df[medium].value_counts(sort=True, normalize=True))
    print('-------------------------------------------\n')
    #YOUR CODE HERE
    plt.show()


# And instead of (or in addition to) the plt.show(), you can also save these plots to your folder on your computer. These are very high quality images then, that could be used in a piece (if you provided appropriate axis titles, etc.), and you can specify the figure size and DPI.
# 
# Note here we've added a 'figsize' specification to the end of the plot method in your missing line of code. You can play around with different figure sizes to see what happens, if you display them here using plt.show().

# In[20]:


for medium in ['radio','newspaper','tv','internet']:
    print(medium.upper())
    print(df[medium].value_counts(sort=True, normalize=True))
    print('-------------------------------------------\n')
    #YOUR CODE HERE ...(kind='bar', figsize=(6,4))
    plt.savefig('{}.png'.format(medium), dpi=400)
    plt.show()

#Now go check your folder and see if the image files have shown up.
#Note that we have to use the curly brackets and .format(medium) to give 
#the relevant title to each figure. 


# ### Plots grouped by variables
# 
# You can also create comparison histograms, side-by-side, for different values of a variable. For example, let's look at the histogram of internet news use for men and women in this dataset.
# 
# Here, we're using the "by=[' ']" command to specify which grouping variable we want, and again specifying the bins and the figure size, both of which you can play around with.

# In[21]:


df.hist(column='internet', by=['gender'], bins=7, figsize=(10,5))


# ## Statistical tests and subsetting datasets
# 
# Now, if we want to move onto statistical comparisons, we can run our normal, basic statistics here in python as well.  There's no need to import your datset to SPSS to do this, if you want to know whether a specific difference is significant, for example.
# 
# ### T-tests
# 
# Let's start with a t-test, comparing the mean internet news use for men and women that we just examined in the histograms. 
# 
# In order to do this, we have to create two new little dataframes out of our first one - one for men, one for women.
# 
# We are using the ability to filter a dataframe (e.g., `df[df['gender']==1]` to create a dataframe only for males; adding `['internet']` at the end selects only the column for internet). This can be handy to select only relevant data for your story out of a much larger dataset!

# In[22]:


males_internet = df[df['gender']==1]['internet']
females_internet = df[df['gender']==0]['internet']


# Each of these new dataframes can then be described and explored as we do with any pandas dataframe, and using `.describe()`, remember, gives us the mean score (handy for our t-test!).

# In[23]:


males_internet.describe()


# In[24]:


females_internet.describe()


# We see the male mean is 3.02, and the female mean is 2.37.  But we don't know if, based on the sample, this is a significant difference.  We don't want to make misleading claims in our story!  So, run a t-test.  (Specifically, an independent samples t-test.)
# 
# The results return the test statistic, p-value, and the degrees of freedom (in that order). 

# In[25]:


ttest_ind(males_internet,females_internet)


# We see that males use the internet significantly more often than females (that e-08 means the p-value is REALLY tiny). 
# 
# We could also do some pretty-printing if we wanted to, to display this more nicely for ourselves.
# 
# The "._f" specification is how many decimal places; the integer before the colon is the position of the output from the default t-test command.
# 
# And again, here we see the use of ".format()" as a method to input something from the ongoing calculation.

# In[26]:


results = ttest_ind(males_internet,females_internet)
print('t({2:.0f}) = {0:.3f}, p = {1:.3f}'.format(*results))


# Let's look into some continous variables. First of all, let us create one: We make a subset of our dataframe that contains only the media variables, apply the `.mean()` method to it (`axis = 1` means that we want to apply it row-wise), and then we assign the result of this to a new colum in the original dataframe.
# 
# 

# In[27]:


df['meanmedia'] = df[['radio','internet','newspaper','tv']].mean(axis=1)


# In[28]:


#We can then plot this mean media usage (for news) by age, using a scatterplot, e.g.
#Feel free to play around with the color parameters, and remember to use help commands to 
#find out more about formatting these plots.

df.plot.scatter(x='age', y='meanmedia', c='blue')


# There are obviously many more possibilities here, including running a correlation between age and mean media use, for example, or using ANOVAs if you had more than 2 groups to compare, etc.  We don't have time to show all of this to you in class, but remember there is a ton of resources online, so you should just search away to find what you need.  If you have problems understanding specific modules or commands you find online, you can approach us during our open lab sessions with questions as to how to apply these techniques to your own data story.

# ### Before we finish, let's play around with some more graphics
# 
# The seaborn library (which we imported at the beginning) offers a lot of cool stuff.

# First, we'll make a simple correlation matrix of the four media in this datset.

# In[29]:


corrmatrix = df[['internet','tv','radio','newspaper']].corr()


# In[30]:


corrmatrix


# But think of ways that are more useful to display this to audiences, who may not want to deal with a correlation matrix.  Heatmaps are one way to do this:

# In[31]:


sns.heatmap(corrmatrix)


# This looks okay, but is a bit redundant, so it would be great if we could sort of 'white out' the unnecessary (replicated) top triangle of the chart, and use colors that are more intuitive - usually darker means a stronger relationship in a heat map, right?
# 
# Here, note that even Damian (EVEN DAMIAN!) can't reproduce all of this out of his head.  But if you look around online, or use what we show you here and adapt it, you can do a lot of amazing graphics stuff.

# In[32]:


sns.set(style="white")
mask = np.zeros_like(corrmatrix, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
cmap = sns.light_palette("red",as_cmap=True)
sns.heatmap(corrmatrix,mask=mask,cmap=cmap,vmin=0,vmax=.2)


# ## So...
# 
# there are lots of possibilities here. Remember: google is your friend here!
# 

# ## More (non-graded) homework :)
# 
# Using the Iris dataset from last Wednesday, try the following:
# 1. Describe the dataset
# 2. Find the value counts of the 'species' column
# 3. Describe the dataset for each of the species separately.
# 4. Transpose the output for this previous command.
# 5. Create side-by-side histograms of petal length for each species.
# 

# Regardless whether you were able to do that, here's a really cool graphic to show you. In this case, we're plotting petal width by petal length, with a different color for each species.  This also uses the seaborn library (indicated by sns).  Because of the nature of this dataset and the values within it, it works quite well.)

# In[33]:


iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')


# In[34]:


iris.groupby('species').describe().T


# In[35]:


iris.hist(column='petal_length', by=['species'], figsize=(10,5))


# In[36]:


sns.scatterplot(x="petal_width", y="petal_length", hue="species", data=iris)


# 
# 
# 
# 
# ## Appendix: Multivariate statistical analysis
# 
# For those who are interested, here's a brief bit on multivariate analyses.  Here, we're focusing on the same comparison of internet news use between men and women, but first, let's see whether that holds when we control for political interest. 
# 
# Before we can do that, we have to bring in another datset, however, and join it.  You can access this dataset and save it from the following URL: https://raw.githubusercontent.com/damian0604/bdaca/master/ipynb/intpol.csv
# 
# We'll talk more about aggregating/merging datasets in a later session, so for now just go with it.

# In[37]:


# intpol=pd.read_csv('intpol.csv') # if you stored it locally 
intpol=pd.read_csv('https://raw.githubusercontent.com/damian0604/bdaca/master/ipynb/intpol.csv') # if reading it directly from the website


# In[38]:


combined = df.join(intpol)


# In[39]:


combined


# Let's do an OLS regression. In order to do so, we need to define a model and then run it. When defining the model, you create the equation in the following manner:
# * First you include your dependent variable, followed by the ~ sign
# * Then you include the independent variables (separated by the + sign)

# In[40]:


m1 = smf.ols(formula='internet ~ age + gender + education', data=combined).fit()


# In[41]:


m1.summary()


# In[42]:


m2 = smf.ols(formula='internet ~ age + gender + education + intpol', data=combined).fit()
m2.summary()


# We can also do a test to see whether M2 is better than M1 (it is, in this case:)
# (see also http://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLSResults.compare_lr_test.html?highlight=compare_lr_test )
# 

# In[43]:


m2.compare_lr_test(m1)


# ## Hexplots
# 
# We have seen scatterplots at work above. Scatterplots are a cool way to show the relationship between two variables, but they mainly work well if both variables have a lot of different values (say, the money people earn in Euros' (and not in categories!), or the time people spent on Facebook in exact minutes). However, if we have only few possible values (such as the integers from 0 to 7, as in our examples above), the dots in the scatterplot will overlap, and an observation that only occurs one single time looks exactly like an observation that occurs 1000 times.
# 
# A hexplot is very much like a scatterplot, but *the more observations overlap at the same (hexagon-shaped) place in the graph, the darker it gets.*
# 
# To make it even more informative, we add histograms of the two variables in the margin, so that you can immediately get an idea of the distributions. This, again, helps us to understand whether there are just a few (very old, very young) people that behave in some way (no media at all, media every day), or whether it's a general pattern.

# In[44]:


sns.jointplot(combined['age'], combined['meanmedia'] , 
              kind="hex", color="#4CB391")

