import pandas as pd
iris = pd.read_csv('iris.csv')
print(iris.head())


wine_reviews = pd.read_csv('winemag-data-130k-v2.csv', index_col=0)
print(wine_reviews.head())


import matplotlib.pyplot as plt


#Scatter Plot
#To create a scatter plot in Matplotlib we can use the scatter method. We will also create a 
#figure and an axis using plt.subplots so we can give our plot a title and labels.

# create a figure and axis
fig, ax = plt.subplots()
# scatter the sepal_length against the sepal_width
ax.scatter(iris['sepal_length'], iris['sepal_width'])
# set a title and labels
ax.set_title('Iris Dataset')
ax.set_xlabel('sepal_length')
ax.set_ylabel('sepal_width')

#
#Histogram
#In Matplotlib we can create a Histogram using the hist method. 
#If we pass it categorical data like the points column from the wine-review dataset 
#it will automatically calculate how often each class occurs.


# create figure and axis
fig, ax = plt.subplots()
# plot histogram
ax.hist(wine_reviews['points'])
# set title and labels
ax.set_title('Wine Review Scores')
ax.set_xlabel('Points')
ax.set_ylabel('Frequency')


#Bar Chart
#A bar chart can be created using the bar method. 
#The bar-chart isn’t automatically calculating the frequency of a 
#category so we are going to use pandas value_counts function to do this. 
#The bar-chart is useful for categorical data that doesn’t have a lot of different categories 
#(less than 30) because else it can get quite messy.

 # create a figure and axis 
fig, ax = plt.subplots() 
# count the occurrence of each class 
data = wine_reviews['points'].value_counts() 
# get x and y data 
points = data.index 
frequency = data.values 
# create bar chart 
ax.bar(points, frequency) 
# set title and labels 
ax.set_title('Wine Review Scores') 
ax.set_xlabel('Points') 
ax.set_ylabel('Frequency')


#Pandas Visualization
#Pandas Visualization makes it really easy to create plots out of a pandas 
#dataframe and series. 
#It also has a higher level API than Matplotlib and therefore we need less code 
#for the same results.
#
#Pandas can be installed using either pip or conda.

iris.plot.scatter(x='sepal_length', y='sepal_width', title='Iris Dataset')

#line chart
#Line Chart
#To create a line-chart in Pandas we can call <dataframe>.plot.line(). 
#Whilst in Matplotlib we needed to loop-through each column we wanted to plot, 
#in Pandas we don’t need to do this because it automatically plots all available numeric columns 
#(at least if we don’t specify a specific column/s).

iris.drop(['species'], axis=1).plot.line(title='Iris Dataset')


##histogram
#In Pandas, we can create a Histogram with the plot.hist method. 
#There aren’t any required arguments but we can optionally pass some like the bin size.

wine_reviews['points'].plot.hist()

#multiple histograms
iris.plot.hist(subplots=True, layout=(2,2), figsize=(10, 10), bins=20)

##bar chart
#Bar Chart
#To plot a bar-chart we can use the plot.bar() method, 
#  but before we can call this we need to get our data. 
#  For this we will first count the occurrences using the value_count() 
#method and then sort the occurrences from smallest to largest using the sort_index() method.

wine_reviews['points'].value_counts().sort_index().plot.bar()

#It’s also really simple to make a horizontal bar-chart using the plot.barh() method.

wine_reviews['points'].value_counts().sort_index().plot.barh()

# We can also plot other data then the number of occurrences.

wine_reviews.groupby("country").price.mean().sort_values(ascending=False)[:5].plot.bar()
