import pandas as pd
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt

iris = pd.read_csv('iris.csv')
wine_reviews = pd.read_csv('winemag-data-130k-v2.csv', index_col=0)

sns.scatterplot(x='sepal_length', y='sepal_width', data=iris)


# We can also highlight the points by class using the hue argument, which is a lot easier than in Matplotlib.

sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', data=iris)


sns.lineplot(data=iris.drop(['species'], axis=1))

# Histogram
#To create a histogram in Seaborn we use the sns.distplot method. 
#We need to pass it the column we want to plot and it will calculate the occurrences itself. 
#We can also pass it the number of bins, 
#and if we want to plot a gaussian kernel density estimate inside the graph.

sns.distplot(wine_reviews['points'], bins=10, kde=True)


# Bar chart
#In Seaborn a bar-chart can be created using the sns.countplot method and passing it the data.

sns.countplot(wine_reviews['points'])


# Box plots
#A Box Plot is a graphical method of displaying the five-number summary.
# We can create box plots using seaborns 
#sns.boxplot method and passing it the data as well as the x and y column name.


df = wine_reviews[(wine_reviews['points']>=95) & (wine_reviews['price']<1000)]
sns.boxplot('points', 'price', data=df)



# Heatmap
#A Heatmap is a graphical representation of data where the 
#individual values contained in a matrix are represented as colors.
# Heatmaps are perfect for exploring the correlation of features in a dataset.
#
#To get the correlation of the features inside a dataset we can call <dataset>.corr(), 
# which is a Pandas dataframe method. This will give us the correlation matrix.
#
#We can now use either Matplotlib or Seaborn to create the heatmap.

# get correlation matrix
import numpy as np
corr = iris.corr()
fig, ax = plt.subplots()
# create heatmap
im = ax.imshow(corr.values)

# set labels
ax.set_xticks(np.arange(len(corr.columns)))
ax.set_yticks(np.arange(len(corr.columns)))
ax.set_xticklabels(corr.columns)
ax.set_yticklabels(corr.columns)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")


###have numbers
fig, ax = plt.subplots()
im = ax.imshow(corr.values)

# set labels
ax.set_xticks(np.arange(len(corr.columns)))
ax.set_yticks(np.arange(len(corr.columns)))
ax.set_xticklabels(corr.columns)
ax.set_yticklabels(corr.columns)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(corr.columns)):
    for j in range(len(corr.columns)):
        text = ax.text(j, i, np.around(corr.iloc[i, j], decimals=2), ha="center", va="center", color="black")
        

# seaborn makes it easier for heatmap
sns.heatmap(iris.corr(), annot=True)

sns.pairplot(iris)

from pandas.plotting import scatter_matrix

fig, ax = plt.subplots(figsize=(12,12))
scatter_matrix(iris, alpha=1, ax=ax)