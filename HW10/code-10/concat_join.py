#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:07:28 2024

@author: payampourashraf
"""

import pandas as pd

# Sample dataframes
df1 = pd.DataFrame({'A': ['A0', 'A1'], 'B': ['B0', 'B1']})
df2 = pd.DataFrame({'A': ['A2', 'A3'], 'B': ['B2', 'B3']})

# Concatenate vertically
vertical_concat = pd.concat([df1, df2], axis=0)

print("Vertical Concatenation:")
print(vertical_concat)

# Concatenate horizontally
horizontal_concat = pd.concat([df1, df2], axis=1)

print("\nHorizontal Concatenation:")
print(horizontal_concat)

# Sample dataframes with different columns and same index
df3 = pd.DataFrame({'C': ['C0', 'C1'], 'D': ['D0', 'D1']}, index=[1, 2])

# Join df1 and df3
joined_df = df1.join(df3)

print("Joined DataFrame:")
print(joined_df)

