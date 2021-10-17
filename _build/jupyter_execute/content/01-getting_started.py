#!/usr/bin/env python
# coding: utf-8

# # On Jupyter Notebooks
# 
# *Written by Damian Trilling, Penny Sheets, Frederic Hopp*
# 
# This notebook is meant to show you what you can do with a Jupyter Notebook. Feel free to play around!

# ## Downloading this notebook
# 
# You can download any notebook from this site simply by navigating to the download button on the top-right corner and then right-clicking on the .ipynb button and selecting "save link as". This allows you to directly save this notebook to a location on your computer. Alternatively, you can find all of these notebooks on the corresponding [Github](https://github.com/fhopp/data_journalism) page. Github is a very popular platform to share code and it has a central role in open-source software development and in open science. People who want to make their data analyses transparent usually share their code here.
# 
# To execute this notebook on your local machine, make sure to open FROM WITHIN a Jupyter Notebook session on your computer.

# ***

# ## Cell types
# 
# There are different types of cells: Code cells and Markdown (or "Text" in Colab) cells (there are two more, but they are not necessary for our purposes). Markdown/Text cells contain text, and code cells contain, well, code. You can edit a cell by double-clicking on it. 
# 
# 
# To 'run' a cell in Anaconda (in the case of markdown/text, to format it), press CTRL-Enter. (You can also hit 'run' up in the menu buttons.)
# 
# **Note:** Depending on your keyboard layout and configuration, cells might also be exectuable by hitting SHIFT+Enter. 
# 
# Try it out now!  Double click on this cell, and then hit CTRL-Enter to format it in Anaconda.
# 
# (**Tip**  If you press CTRL-Enter and nothing happens, then it most likely means you're not in a Markdown/Text cell, but some other kind of cell.)
# 
# If you want to know more about formatting with markdown, have a look at 
# https://guides.github.com/features/mastering-markdown/

# This is a markdown cell.  Write whatever you want in it.

# ## To create a new cell in Anaconda
# ...You hit the 'plus sign' button up on the top left of jupyter notebook, at the toolbar.  By default, this is a code cell.  But you can change it to a markdown cell at the dropdown menu to the right of that same toolbar.  Try creating a new markdown cell below this.  Don't forget control+enter to format it.  (You can also move cells around, using the up and down arrows up in the menus above.)
# 
# # Note that there are various ways to format things; using hashtags allows for bigger, bolder fonts.
# 
# ### More hashtags, smaller fonts, but still bigger and bolder than no-hashtags.
# 
# Try creating your new markdown/text cell below here.

# ## Running Python code in Jupyter
# 
# Now we can start with some actual python commands, actual code, instead of markdown/text. 
# 
# Let's try to print something... don't forget to hit control+enter to run the command (or run it through a button).
# 
# Once a line of code has been run, a number appears next to it (in sequential order).  This can be very useful for knowing whether you've run code already or not - relevant to when we install certain packages, e.g., or you search for or name specific datasets.  

# In[1]:


print('Hello world')


# Now create your own print command in the next cell.  Print whatever you want.  The key is to make sure you format the command correctly - you need parentheses and quotation marks, and to be sure all are closed out afterward. Python helps you with this quite a bit (for example, look at how the colors change if you format something (in-)correctly), but, you have to practice.

# In[ ]:





# In[2]:


#Note, in a code cell, you can also preface a line of text with a hashtag, and python will ignore it as code.
#This can be useful for very short notes within particular code cells, rather than creating separate markdown/text cells.
#But watch the lenghth of your cells!


# Python also allows us to do very simple calculations.  Just tell it the values and make it do the work:

# In[3]:


a = 5
b = 10
c = a + b
print(c)


# Many commands have output, but some won't (just loading a package of tools, or a dataset, e.g.).  But remember to check the number next to the cell to see if you've actually run those cells or not.  Often, you have to start back at the begining because you missed a simple but important step.  
# 
# **Good to know:** you can always clear what you've done and re-run various (or all) cells, by using the "cell" menu in Anaconda.
# 
# **Note** If you clear everything, then all imported data and modules (see next point) are also cleared.  So you can't just start running your commands in the middle of the notebook; you'll often have to go back to the earlier cells to start from scratch.  (Since the code is already written, this takes literally only seconds sometimes to get back to where you were.)
# 

# ***

# ## Importing Modules
# 
# Because we want to do a lot more than printing words and running simple calculations, we can import modules that help us do fancier things -- and in particular, help us to read data easily.  Our main module in this course is called "pandas".  Whenever you import anything into Python, it needs to have a name.  You can either leave the original name - pandas - (by just typing `import pandas`) or shorten that name so you don't have to type it again and again and again.  So one shorthand that is commonly used is `pd` for pandas.  Try importing it now with the following command.  You'll see that no output appears, but you should - if you've run it correctly - end up with a number next to the command line.

# In[5]:


import pandas as pd


# We'll explain a bit more about pandas in class, but, pandas basically allows us to work with data more easily.  So anytime you see a command that follows here that has 'pd' in the line of code, it means pandas is at work.
# 
# Here, pandas can help us read in a dataset from the web, just a random dataset that is often used to illustrate things like statistical programming. The command is simply `pd.read_` and then the type of the file, and its url.  In this case, it is a csv file, but python can also read many other types of files--we'll address more of those in a minute.
# 
# In this case, the dataset comes from the url listed here, and, because the dataset is originally called 'iris', we will also tell python to call the dataset `iris`.  But we could call it anything else we want.
# 
# As for the second line of code here, if we just type the name of the dataset after having read it into jupyter, it also displays a bunch of the dataset for us to see.  This is handy, as long as you don't have insanely huge datasets.

# In[6]:


iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
iris


# ### Methods
# In Python, basically everything is an "object". That's also why we assign names to them: It makes the objects re-usable. In the cell above, we created an object (more specifically, a pandas dataframe) that we called `iris`.
# 
# Objects can have "methods" that are associated with them. Pandas dataframes, for example, have some methods that allow you to directly run some simple analyses on them. One of them is `.describe()`.
# 
# Note the `()` at the end. If you want to "call" (= execute, run) a method, you need to end with these parentheses. They also allow you to give some additional "arguments" (parameters, options). Compare the following two method calls:

# In[7]:


iris.describe()


# In[8]:


iris.describe(percentiles=[0.1, 0.9])


# One more note: as with SPSS and syntax help, python is happy to help you.  You can type a command and then put a question mark after it, and it'll explain that command to you.  Try it here:

# In[9]:


get_ipython().run_line_magic('pinfo', 'iris.describe')


# ### Functions
# 
# Next to methods, there are also functions. Just like methods, functions take one or more "arguments" (i.e., some input) between `()`. They then return some output. But unlike methods, they are not directly associated with an object.
# 
# You already know one function: `print()`.
# 
# Let's try out some functions.  First, create two objects to play with:

# In[10]:


mystring = "Hello world"
mylist = [22, 3, 4]


# Now, try out the following functions and try to explain what they do to those objects.  What are these functions trying to do?

# In[11]:


len(mystring)


# In[12]:


len(mylist)


# In[13]:


sum(mylist)


# Now, let's combine these techniques.
# Each string has the method `.split()` that splits it into words. With this knowledge, can you calculate the number of words in `mystring` by using the output of this method as input for the `len()` function?

# In[ ]:





# # You see...
# 
# It's actually not that difficult. It can seem overwhelming to not know the codes for things, but, that's what we're going to teach you.  And there are tons of resources online to help, as well (check the resources tab on the left!). 
# 
# What's wonderful about jupyter notebook is that we have code, results, and explanation/notes in one single file.  You will also format your assignments this way, using markdown cells to provide notes.  The 'output' or results don't matter that much in the file itself, because we can always re-run the code each time we open your files.  But the markdown and code cells are essential.
# 
# We are looking forward to exploring the possibilities of Jupyter Notebook, Python, and Pandas with you in the next weeks!

# ***
