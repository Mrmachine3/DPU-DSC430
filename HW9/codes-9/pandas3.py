# https://www.geeksforgeeks.org/working-with-missing-data-in-pandas/
import pandas as pd 
  
# importing numpy as np 
import numpy as np 
  
# dictionary of lists 
dict = {'First Score':[100, 90, np.nan, 95], 
        'Second Score': [30, 45, 56, np.nan], 
        'Third Score':[np.nan, 40, 80, 98]} 
  
# creating a dataframe from list 
df = pd.DataFrame(dict) 
  
# using isnull() function   
df.isnull()


  
# using notnull() function  
df.notnull() 

df.fillna(0) 



  
# dictionary of lists 
dict = {'First Score':[100, 90, np.nan, 95], 
        'Second Score': [30, np.nan, 45, 56], 
        'Third Score':[52, 40, 80, 98], 
        'Fourth Score':[np.nan, np.nan, np.nan, 65]} 
  
# creating a dataframe from dictionary 
df = pd.DataFrame(dict) 
  
# using dropna() function   
df.dropna() 


# dictionary of lists 
dict = {'First Score':[100, np.nan, np.nan, 95], 
		'Second Score': [30, np.nan, 45, 56], 
		'Third Score':[52, np.nan, 80, 98], 
		'Fourth Score':[np.nan, np.nan, np.nan, 65]} 

df = pd.DataFrame(dict) 

# using dropna() function	 
df.dropna(how = 'all') 


# dictionary of lists 
dict = {'First Score':[100, np.nan, np.nan, 95], 
        'Second Score': [30, np.nan, 45, 56], 
        'Third Score':[52, np.nan, 80, 98], 
        'Fourth Score':[60, 67, 68, 65]} 
  
# creating a dataframe from dictionary   
df = pd.DataFrame(dict) 
  
# using dropna() function      
df.dropna(axis = 0, how = 'any') 