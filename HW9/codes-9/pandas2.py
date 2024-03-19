
#https://www.datacamp.com/community/blog/python-pandas-cheat-sheet
import pandas as pd

s = pd.Series([3, -5, 7, 4],  index=['a',  'b',  'c',  'd'])

data = {'Country': ['Belgium',  'India',  'Brazil'],

'Capital': ['Brussels',  'New Delhi',  'Brasilia'],

'Population': [11190846, 1303171035, 207847528]}

df = pd.DataFrame(data,columns=['Country',  'Capital',  'Population'])


s['b'] #Get one element

df[1:]  #Get subset of a DataFrame

df.iloc([0][0])

df.loc['Country']

s[~(s > 1)]

df[df['Population']>1200000000]

df.sort_values(by='Country') 

df.shape

df.columns
df.info()

df.count()  # Number of non-NA values
df.sum()
df.min()/df.max()

Total = df['Population'].sum()