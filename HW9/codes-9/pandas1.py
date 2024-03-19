#https://www.learnpython.org/en/Pandas_Basics
dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd
brics = pd.DataFrame(dict)
print(brics)

# Set the index for brics
brics.index = ["BR", "RU", "IN", "CH", "SA"]

# Print out brics with new index values
print(brics)

####
# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv('cars.csv')

# Print out cars
print(cars)

####
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out mpg column as Pandas Series
print(cars['mpg'])

# Print out mpg column as Pandas DataFrame
print(cars[['mpg']])

# Print out DataFrame with mpg and cyl columns
print(cars[['mpg', 'cyl']])


print(cars[0:4])

# Print out fifth, sixth, and seventh observation
print(cars[4:6])

print(cars.iloc[2])

"""
You can also use loc and iloc to perform just about any data selection operation. 
loc is label-based, which means that you have to specify rows and columns based on their row 
and column labels. iloc is integer index based, so you have to specify rows and columns by 
their integer index like you did in the previous exercise.
"""
print(cars.loc['Mazda RX4'])