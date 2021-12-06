#!/usr/bin/env python
# coding: utf-8

# # 9. Interactive Data Visualization
# 
# *Frederic Hopp and Penny Sheets*
# 
# This notebook gives some examples for how to create interactive visualizations for the web.
# 
# We will use the following two visualization packages:
# - `bokeh`
# - `pygal`
# 
# 
# `bokeh` allows you to create interactive visualizations in which users can hover over elements, zoom in, etc.
# `pygal` allows you to create standard charts with hover-effects.
# 
# 
# ## Download the sample data
# The first time you run this notebook, you will need to download some example data.
# You only need to do this once, and should "comment out" (put hashtags in front of) the following two lines again after running them once.

# In[ ]:


import bokeh
bokeh.sampledata.download()


# In[ ]:


pip install cairosvg


# # Interactivity 
# 
# As discussed in the literature of week 4, interactivity should have a function. For instance, it can be used to reduce information overload while still providing information 'on demand' if users want to dig into it.
# 
# Consider the example below (under the bokeh section), where the user at a first glance can get an idea of the geographical distribution of unemployment, but if they really want to know more, can even get the exact number for each and every county by hovering over it.
# 
# More complicated online demos of bokeh apps are available here:
# 
# - https://demo.bokeh.org/movies
# - https://demo.bokeh.org/weather
# 

# ### But first, we'll start with an example using pygal
# 
# For more info and examples, see http://www.pygal.org .
# 
# It will make your bar charts etc. just a bit more attractive by allowing things like displaying values when hovering over columns with the mouse.

# In[ ]:


import pygal
import bokeh
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


# First we create a bar graph object (this is sort of like how we did in Seaborn, creating a blank canvas 
# before telling it what to put on that canvas.)

mylittlebar_chart = pygal.Bar()                                            

# Next we add some values to it; in this case, we're adding the Fibonacci number sequence, and labeling it accordingly.
mylittlebar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
mylittlebar_chart.add('Pinocchio', [1, 2, 3, 4, 8, 9, 12, 10, 8, 5, 2])


# In[ ]:


# With pygal, you can render this into an .svg visualization for display in your web browser.

mylittlebar_chart.render_in_browser()

# or you can save to a file for later embedding/placement wherever you want it:
# bar_chart.render_to_file('bar_chart.svg') 


# In[ ]:


mylittlebar_chart.render_sparktext()


# In[ ]:


#this thing is often used for economic publications.  also note that with the html code,
#if you open in a notebook, all the goodies are there in the svg file, you don't have to
#also upload your data anywhere.  (i think)


# Let's do this with our own data that we used in an earlier notebook.
# We first do it the old-fashioned way that we already know, then we use pygal instead.

# In[ ]:


mediause = pd.read_csv('https://raw.githubusercontent.com/damian0604/bdaca/master/ipynb/mediause.csv') # if directly reading it from source 
mediause


# In[ ]:


frequency_of_internet_use = mediause['internet'].value_counts().sort_index()
frequency_of_internet_use


# In[ ]:


frequency_of_internet_use.plot(kind='bar')


# In[ ]:


bar_chart = pygal.Bar()                                            

frequency_of_internet_use = mediause['internet'].value_counts().sort_index()
frequency_of_tv_use = mediause['tv'].value_counts().sort_index()
frequency_of_newspaper_use = mediause['newspaper'].value_counts().sort_index()

#bar_chart.x_labels = range(8)
#or, for getting x-axis labels.
bar_chart.x_labels = frequency_of_internet_use.index
# Next we add some values to it; in this case, we're adding the Fibonacci number sequence, and labeling it accordingly.
bar_chart.add('internet', frequency_of_internet_use)
bar_chart.add('tv', frequency_of_tv_use)
bar_chart.add('newspaper', frequency_of_newspaper_use)


# In[ ]:


bar_chart.render_in_browser()


# ### An example with bokeh
# 
# This one is taken from an existing demo online (on the website of bokeh), to show bokeh's capacities.  But all documentation and further info can be found at the link here, for more info & examples: https://bokeh.org/

# In[ ]:


from bokeh.io import show, output_file
from bokeh.models import LogColorMapper
from bokeh.palettes import Viridis6 as palette
from bokeh.plotting import figure

from bokeh.sampledata.us_counties import data as counties
from bokeh.sampledata.unemployment import data as unemployment


# In[ ]:


type(counties)
#if you look through both these, you see there are identifiers per county


# In[ ]:


counties = {
    code: county for code, county in counties.items() if county["state"] == "ca"
}

county_xs = [county["lons"] for county in counties.values()]
county_ys = [county["lats"] for county in counties.values()]

county_names = [county['name'] for county in counties.values()]
county_rates = [unemployment[county_id] for county_id in counties]
color_mapper = LogColorMapper(palette=palette)

data=dict(
    x=county_xs,
    y=county_ys,
    name=county_names,
    rate=county_rates,
)

TOOLS = "pan,wheel_zoom,reset,hover,save"

p = figure(
    title="California Unemployment, 2009", tools=TOOLS,
    x_axis_location=None, y_axis_location=None,
    tooltips=[
        ("Name", "@name"), ("Unemployment rate)", "@rate%"), ("(Long, Lat)", "($x, $y)")
    ])
p.grid.grid_line_color = None
p.hover.point_policy = "follow_mouse"

p.patches('x', 'y', source=data,
          fill_color={'field': 'rate', 'transform': color_mapper},
          fill_alpha=0.7, line_color="white", line_width=0.5)



# save to file
output_file('bokeh-example.html')

# and/or show in browser
show(p)


# In[ ]:


from bokeh.io import show, output_file
from bokeh.models import LogColorMapper
from bokeh.palettes import Viridis6 as palette
from bokeh.plotting import figure

from bokeh.sampledata.us_counties import data as counties
from bokeh.sampledata.unemployment import data as unemployment

counties = {
    code: county for code, county in counties.items() if county["state"] == "mn"
}

county_xs = [county["lons"] for county in counties.values()]
county_ys = [county["lats"] for county in counties.values()]

county_names = [county['name'] for county in counties.values()]
county_rates = [unemployment[county_id] for county_id in counties]
color_mapper = LogColorMapper(palette=palette)

data=dict(
    x=county_xs,
    y=county_ys,
    name=county_names,
    rate=county_rates,
)

TOOLS = "pan,wheel_zoom,reset,hover,save"

p = figure(
    title="Minnesota Unemployment, 2009", tools=TOOLS,
    x_axis_location=None, y_axis_location=None,
    tooltips=[
        ("Name", "@name"), ("Unemployment rate)", "@rate%"), ("(Long, Lat)", "($x, $y)")
    ])
p.grid.grid_line_color = None
p.hover.point_policy = "follow_mouse"

p.patches('x', 'y', source=data,
          fill_color={'field': 'rate', 'transform': color_mapper},
          fill_alpha=0.7, line_color="white", line_width=0.5)



# save to file
# underlying data, again, already in this html code; don't need to worry about publishing it.
# code/data are fetched automatically through bokeh servers.
output_file('bokeh-example.html')

# and/or show in browser
show(p)


# # Publishing interactivity
# 
# Publishing and distributing your STATIC visualizations is straightforward (see week 4 of this course). You can simply save them in any format you like (e.g., `.png` (better than `.jpg` for text and sharp lines), or as a vector graphic (e.g., `.svg`) that allows loss-free scaling.
# For example, we could use `plt.save_fig()` for that purpose.
# 
# This file, then, can be freely used in any online or offline publication.
# 
# But how can we do this online? It's one thing to make a nice interactive visualization in *your* browser, it's another thing to share them with the world.
# 
# ## SVG graphics
# 
# 
# One approach are SVG graphics. That's the route we took in the pygal example above. As you see, you can just open the file in any browser, and the interactive elements (hovering over the bars with your mouse shows the values) work.
# 
# However, there is one problem with this approach: First, the possibilities types of interactivity possible are a bit limited. Second, and more importantly: SVG graphics are sometimes seen as a security risk (because one could construct a malicious svg file that executes unwanted code); and therefore, many platforms restrict their use (for instance, Wordpress - although you can (partly) circumvent this, for instance by installing a svg plugin).
# 
# If you build your own website from scratch, that's less of a problem, of course.
# 
# Here, you can find an example of how to embed svg graphics in a web page:
# http://www.pygal.org/en/stable/documentation/web.html
# 
# 
# ## JavaScript (client-side)
# 
# The bokeh example above takes a different approach: It generates an HTML file and java script code that then is used to render the interactive graphic in the users' browser. That means that if we distribute the HTML file (and, for instance, upload it to our own website; I did it [here](http://www.damiantrilling.net/downloads/test.html)), anyone can use it in their browser.
# 
# It requires a bit more fiddling, though, to display such a thing inline (for instance, like embedding a picture within a wordpress blog). With a bit of HTML knowledge, though, you can get there.
# You can find a lot of (free) HTML tutorials online.
# 
# 
# ## Server-side approaches
# 
# Both approaches outlined above are *self-contained*: They include all data, all calculations are already made, etc. Especially if you have very large data, or when you want to actually run some python code based on the user input, you will need to run your own (bokeh-) server. That's a cool thing to do (and a nice project to pursue, if you want to experiment a bit), but out of scope for this class.

# # Exercise
# 
# The example below is from the official bokeh tutorial (https://mybinder.org/v2/gh/bokeh/bokeh-notebooks/master?filepath=tutorial%2F00%20-%20Introduction%20and%20Setup.ipynb ). It plots a complex chart with intearctive hover.
# 
# **Try to understand the code (in broad lines) and modify it to explore what happens. Construct a different visualization, or use other (own?) data.**

# In[ ]:


# import modules and prepare example dataset

from bokeh.models import ColumnDataSource, HoverTool
from bokeh.plotting import figure
from bokeh.sampledata.autompg import autompg_clean as df
from bokeh.transform import factor_cmap

df.cyl = df.cyl.astype(str)
df.yr = df.yr.astype(str)


# In[ ]:


df


# In[ ]:


group = df.groupby(by=['cyl', 'mfr'])
source = ColumnDataSource(group)

p = figure(plot_width=800, plot_height=300, title="Mean MPG by # Cylinders and Manufacturer",
           x_range=group, toolbar_location=None, tools="")

p.xgrid.grid_line_color = None
p.xaxis.axis_label = "Manufacturer grouped by # Cylinders"
p.xaxis.major_label_orientation = 1.2

index_cmap = factor_cmap('cyl_mfr', palette=['#2b83ba', '#abdda4', '#ffffbf', '#fdae61', '#d7191c'], 
                         factors=sorted(df.cyl.unique()), end=1)

p.vbar(x='cyl_mfr', top='mpg_mean', width=1, source=source,
       line_color="white", fill_color=index_cmap, 
       hover_line_color="darkgrey", hover_fill_color=index_cmap)

p.add_tools(HoverTool(tooltips=[("MPG", "@mpg_mean"), ("Cyl, Mfr", "@cyl_mfr")]))

show(p)


# To give you a little help, I made one with our mediause dataset:

# In[ ]:


group = mediause.groupby('education')
source = ColumnDataSource(group)

p = figure()
p.vbar(x='education', top='internet_mean', width=1, source=source,
       line_color="white")

p.add_tools(HoverTool(tooltips=[("internet use", "@internet_mean"), ("education", "@education")]))

show(p)


# In[ ]:





# In[ ]:


mediause_nice = mediause.copy()
mediause_nice['education'].replace({1: 'basis', 2:'vmbo', 3: 'vmbo-t', 4: 'mbo', 5: 'hbo', 6:'wo-bachelor',
                               7:'wo-master'}, inplace=True)


group = mediause_nice.groupby('education')
source = ColumnDataSource(group)

p = figure(x_range=group)
p.vbar(x='education', top='internet_mean', width=1, source=source,
       line_color="white")

p.add_tools(HoverTool(tooltips=[("internet use", "@internet_mean"), ("education", "@education")]))

show(p)


# In[ ]:


group.describe()

