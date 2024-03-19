#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:06:07 2024

@author: payampourashraf
"""

import pandas as pd

# Creating two dataframes
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                    'B': ['B0', 'B1', 'B2']})

df2 = pd.DataFrame({'A': ['A3', 'A4', 'A5'],
                    'B': ['B3', 'B4', 'B5']})

# Concatenating dataframes
vertical_concat = pd.concat([df1, df2])

print(vertical_concat)

horizontal_concat = pd.concat([df1, df2], axis=1)

print(horizontal_concat)

df3 = pd.DataFrame({'C': ['C0', 'C1', 'C2'],
                    'D': ['D0', 'D1', 'D2']},
                   index=[2, 3, 4])

vertical_concat_diff_index = pd.concat([df1, df3])

print(vertical_concat_diff_index)

concat_reset_index = pd.concat([df1, df3], ignore_index=True)

print(concat_reset_index)


import pandas as pd

# Creating two dataframes with different indexes
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                    'B': ['B0', 'B1', 'B2']},
                   index=[0, 1, 2])

df2 = pd.DataFrame({'C': ['C0', 'C1', 'C2'],
                    'D': ['D0', 'D1', 'D2']},
                   index=[1, 2, 3])

# Concatenating horizontally
horizontal_concat = pd.concat([df1, df2], axis=1)

print(horizontal_concat)

