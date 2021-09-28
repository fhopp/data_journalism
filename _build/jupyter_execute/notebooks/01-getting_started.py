#!/usr/bin/env python
# coding: utf-8

# # Getting Started
# ## Wednesday, week 1, part 1: getting started with Jupyter Notebooks
# 
# *Damian Trilling and Penny Sheets*
# 
# This notebook is meant to show you what you can do with a Jupyter Notebook. Feel free to play around!

# ## Downloading this notebook from github
# 
# You can find this file on github. Github is a very popular platform to share code and it has a central role in open-source software development and in open science. People who want to make their data analyses transparent usually share their code here.
# 
# ### If you use Anaconda on your computer
# 
# Usually, people *clone* or maybe download whole repositories (projects) from github (and, in fact, you can do so to if you want to), but if you just want to have a single file (such as this one), then you can get it as follows:
# 
# 1. Click on the file to view it on Github. (It may show an error, but this is okay; what is important is to have access to the 'raw' file, not to be able to preview it in Github.)
# 2. Click on the "Raw" button in the upper right corner
# 3. Depending on your system, the file either downloads directly or you see the raw computer code behind this. That's fine, just click on "File/save as" in your browser, or right-click.
# 4. It is *very important* that you do *not* choose 'HTML', 'web page' or something similar in Save-as-dialogue. Choose "All files (\*.\*)" or similar as file type, and make sure that the filename ends in ".ipynb".  Also try to do "all files" instead of a text file.  Know where it is that you save the file, of course, on your computer.  It's probably wisest to create one folder for our class and keep everything there.
# 5. Open the downloaded file FROM WITHIN in Jupyter Notebook on your computer.
# 
# ### If you use google Colab
# 
# Colab will allow you to run things through the cloud.  You can interface directly with Github from there, and it seems to keep track of your files within your Colab space.  You can aslo save things to Google Drive from within Colab.  We'll talk more about the benefits & drawbacks of Colab and Anaconda in class during week 1.
# 
# 1. Within the basic welcome Colaboratory screen, you can click on "File - Open Notebook"
# 2. Then click over to the Github tab, and simply paste in our github page address: https://github.com/uvacw/datajournalism
# 3. Within there the various notebooks will appear, including this one - click on it to open it within Colab and you're off to the races.
# 4. BUT!  You need to make a copy of the notebook for yourself before you can edit it/play around.  So, do that first.  You should save in Drive, and then you'll re-access the notebook not by going to Github, but by going to the "drive" tab at the File - Open Notebook option.
# 

# ## Cell types
# 
# There are different types of cells: Code cells and Markdown (or "Text" in Colab) cells (there are two more, but they are not necessary for our purposes). Markdown/Text cells contain text, and code cells contain, well, code. You can edit a cell by double-clicking on it. 
# 
# 
# To 'run' a cell in Anaconda (in the case of markdown/text, to format it), press CTRL-Enter. (You can also hit 'run' up in the menu buttons.)
# 
# In Colab, you can simply double-dlick the previewed version of the text cell to format it.  To run a code cell, you can do ctrl+enter or you can hit the run arrow next to the cell.
# 
# Try it out now!  Double click on this cell, and then hit CTRL-Enter to format it in Anaconda, or in Colab just click on the right-hand preview of the cell.
# 
# (Tip!!  If you press CTRL-Enter and nothing happens, then it most likely means you're not in a Markdown/Text cell, but some other kind of cell.)
# 
# If you want to know more about formatting with markdown, have a look at 
# https://guides.github.com/features/mastering-markdown/

# This is a markdown cell.  Write whatever you want in it.

# ## To create a new cell in Anaconda
# ...You hit the 'plus sign' button up on the top left of jupyter notebook, at the toolbar.  By default, this is a code cell.  But you can change it to a markdown cell at the dropdown menu to the right of that same toolbar.  Try creating a new markdown cell below this.  Don't forget control+enter to format it.  (You can also move cells around, using the up and down arrows up in the menus above.)
# 
# ## To create a new cell in Colab
# ...You just hit either +code or +text in the upper left.
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

# In[ ]:


print('Hello world')


# Now create your own print command in the next cell.  Print whatever you want.  The key is to make sure you format the command correctly - you need parentheses and quotation marks, and to be sure all are closed out afterward. Python helps you with this quite a bit (for example, look at how the colors change if you format something (in-)correctly), but, you have to practice.

# In[ ]:





# In[ ]:


#Note, in a code cell, you can also preface a line of text with a hashtag, and python will ignore it as code.
#This can be useful for very short notes within particular code cells, rather than creating separate markdown/text cells.
#But watch the lenghth of your cells!


# Python also allows us to do very simple calculations.  Just tell it the values and make it do the work:

# In[ ]:


a = 5
b = 10
c = a + b
print(c)


# Many commands have output, but some won't (just loading a package of tools, or a dataset, e.g.).  But remember to check the number next to the cell to see if you've actually run those cells or not.  Often, you have to start back at the begining because you missed a simple but important step.  
# 
# Good to know: you can always clear what you've done and re-run various (or all) cells, by using the "cell" menu in Anaconda, or by using "edit" and "runtime" menus in Colab.
# 
# **Just note! If you clear everything, then all imported data and modules (see next point) are also cleared.  So you can't just start running your commands in the middle of the notebook; you'll often have to go back to the earlier cells to start from scratch.  (Since the code is already written, this takes literally only seconds sometimes to get back to where you were.)
# 

# ## Importing Modules
# 
# Because we want to do a lot more than printing words and running simple calculations, we can import modules that help us do fancier things -- and in particular, help us to read data easily.  Our main module in this course is called "pandas".  Whenever you import anything into Python, it needs to have a name.  You can either leave the original name - pandas - (by just typing `import pandas`) or shorten that name so you don't have to type it again and again and again.  So one shorthand that is commonly used is `pd` for pandas.  Try importing it now with the following command.  You'll see that no output appears, but you should - if you've run it correctly - end up with a number next to the command line.

# In[ ]:


import pandas as pd


# We'll explain a bit more about pandas in class, but, pandas basically allows us to work with data more easily.  So anytime you see a command that follows here that has 'pd' in the line of code, it means pandas is at work.
# 
# Here, pandas can help us read in a dataset from the web, just a random dataset that is often used to illustrate things like statistical programming. The command is simply `pd.read_` and then the type of the file, and its url.  In this case, it is a csv file, but python can also read many other types of files--we'll address more of those in a minute.
# 
# In this case, the dataset comes from the url listed here, and, because the dataset is originally called 'iris', we will also tell python to call the dataset `iris`.  But we could call it anything else we want.
# 
# As for the second line of code here, if we just type the name of the dataset after having read it into jupyter, it also displays a bunch of the dataset for us to see.  This is handy, as long as you don't have insanely huge datasets.

# In[ ]:


iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
iris


# ### Methods
# In Python, basically everything is an "object". That's also why we assign names to them: It makes the objects re-usable. In the cell above, we created an object (more specifically, a pandas dataframe) that we called `iris`.
# 
# Objects can have "methods" that are associated with them. Pandas dataframes, for example, have some methods that allow you to directly run some simple analyses on them. One of them is `.describe()`.
# 
# Note the `()` at the end. If you want to "call" (= execute, run) a method, you need to end with these parentheses. They also allow you to give some additional "arguments" (parameters, options). Compare the following two method calls:

# In[ ]:


iris.describe()


# In[ ]:


iris.describe(percentiles=[0.1, 0.9])


# One more note: as with SPSS and syntax help, python is happy to help you.  You can type a command and then put a question mark after it, and it'll explain that command to you.  Try it here:

# In[ ]:


get_ipython().run_line_magic('pinfo', 'iris.describe')


# ### Functions
# 
# Next to methods, there are also functions. Just like methods, functions take one or more "arguments" (i.e., some input) between `()`. They then return some output. But unlike methods, they are not directly associated with an object.
# 
# You already know one function: `print()`.
# 
# Let's try out some functions.  First, create two objects to play with:

# In[ ]:


mystring = "Hello world"
mylist = [22, 3, 4]


# Now, try out the following functions and try to explain what they do to those objects.  What are these functions trying to do?

# In[ ]:


len(mystring)


# In[ ]:


len(mylist)


# In[ ]:


sum(mylist)


# Now, let's combine these techniques.
# Each string has the method `.split()` that splits it into words. With this knowledge, can you calculate the number of words in `mystring` by using the output of this method as input for the `len()` function?

# In[ ]:





# # You see...
# 
# It's actually not that difficult. It can seem overwhelming to not know the codes for things, but, that's what we're going to teach you.  And there are tons of resources online to help, as well.
# 
# What's wonderful about jupyter notebook is that we have code, results, and explanation/notes in one single file.  You will also format your assignments this way, using markdown cells to provide notes.  The 'output' or results don't matter that much in the file itself, because we can always re-run the code each time we open your files.  But the markdown and code cells are essential.
# 
# We are looking forward to exploring the possibilities of Jupyter Notebook, Python, and Pandas with you in the next weeks!

# In[ ]:





# ## Bonus: Accessing your Google Drive from Colab
# 
# (not applicable to Anaconda)
# 
# If you are running this notebook in Google Colab, you can also access your own Google Drive (longer explanation here: https://www.marktechpost.com/2019/06/07/how-to-connect-google-colab-with-google-drive/ ).
# 
# Run this cell and follow the instructions that pop up (follow a link, copy-paste authorization code):

# In[ ]:


from google.colab import drive

drive.mount('/mnt')


# You can now address all files in your google drive by storing things in or loading things from the folder `/mnt/My Drive`.
# 
# **In other words: Typing `/mnt/My Drive/` as first part of a file name simply links to your Google Drive. If you have a file `iris.csv` in a folder `datajournalism` on your Google Drive, then you can access it with
# `/mnt/My Drive/datajournalism/iris.csv`**
# 
# (Nerd note: '/mnt' is kind of arbitrary. We could use a different name, but we chose that name because it commonly stands for "mount"-ed file systems - files that are in fact stored somewhere else but made accessible as if they were local)
# 
# Thus, `/mnt/My Drive/datajournalism/iris.csv` is the GoogleColab way of specifiying that you want to access this file:

# In[1]:


from IPython.display import Image
Image("https://github.com/uvacw/datajournalism/raw/master/googledrive1.png")


# Let's write the iris dataset we loaded above to our google drive (just in the main folder):

# In[ ]:


iris.to_csv('/mnt/My Drive/iris.csv')


# You can of course also create (or access) subfolders in your drive. Let's make a folder "datajournalism" on your drive. We are first importing to modules for creating folders and for displaying folder contents. You do not need to remember these - this is just to show you what can be done. You can as well use the Google Drive web interface

# In[ ]:


import os
from glob import glob

os.mkdir("/mnt/My Drive/datajournalism")
iris.to_csv('/mnt/My Drive/datajournalism/iris.csv')
print("All CSV files in my data journalism folder:")
print(glob("/mnt/My Drive/datajournalism/*.csv"))

