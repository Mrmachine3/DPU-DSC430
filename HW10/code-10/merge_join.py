#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:09:02 2024

@author: payampourashraf
"""
import pandas as pd

df1 = pd.DataFrame({'key': ['K0', 'K1', 'K2'], 'A': ['A0', 'A1', 'A2']})
df2 = pd.DataFrame({'key': ['K0', 'K1', 'K2'], 'B': ['B0', 'B1', 'B2']})

# Merging on a common column
merged_df = pd.merge(df1, df2, on='key', how = 'outer')

print(merged_df)


df3 = pd.DataFrame({'left_key': ['K0', 'K1', 'K2'], 'A': ['A0', 'A1', 'A2']})
df4 = pd.DataFrame({'right_key': ['K0', 'K1', 'K2'], 'B': ['B0', 'B1', 'B2']})

# Merging with different keys
merged_df2 = pd.merge(df3, df4, left_on='left_key', right_on='right_key')

print(merged_df2)


df5 = pd.DataFrame({'key': ['K0', 'K1', 'K3'], 'A': ['A0', 'A1', 'A3']})

# Left join
left_joined = pd.merge(df1, df5, on='key', how='left')

print("Left Join:")
print(left_joined)

# Right join
right_joined = pd.merge(df1, df5, on='key', how='right')

print("\nRight Join:")
print(right_joined)

# Outer join
outer_joined = pd.merge(df1, df5, on='key', how='outer')

print("\nOuter Join:")
print(outer_joined)

