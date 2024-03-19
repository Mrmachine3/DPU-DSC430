#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:05:24 2024

@author: payampourashraf
"""

import pandas as pd

# Creating two dataframes
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                    'B': ['B0', 'B1', 'B2']},
                   index=['K0', 'K1', 'K2'])

df2 = pd.DataFrame({'C': ['C0', 'C1', 'C2'],
                    'D': ['D0', 'D1', 'D2']},
                   index=['K0', 'K2', 'K3'])

# Joining df1 and df2
joined_df = df1.join(df2, how = 'outer')

print(joined_df)

df3 = pd.DataFrame({'E': ['E0', 'E1', 'E2'],
                    'F': ['F0', 'F1', 'F2']},
                   index=['K0', 'K1', 'K2'])

joined_df2 = df1.join(df3)

print(joined_df2)

# Outer join
outer_joined = df1.join(df3, how='outer')

print(outer_joined)
