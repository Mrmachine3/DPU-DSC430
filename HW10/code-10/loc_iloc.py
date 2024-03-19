#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 15:58:06 2024

@author: payampourashraf
"""

import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [24, 30, 35, 40, 23],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Miami', 'Seattle']
}
df = pd.DataFrame(data, index=['a', 'b', 'c', 'd', 'e'])


print(df.iloc[0])

print(df.iloc[1:3])

print(df.iloc[1, -1])

print(df.loc['b'])

print(df.loc['b':'d'])

print(df.loc['c', 'Age'])

print(df.loc['a':'c', ['Name', 'City']])
