import pandas as pd

# Sample dataframes
df1 = pd.DataFrame({'key': ['K0', 'K1', 'K2'], 'A': ['A0', 'A1', 'A2']})
df2 = pd.DataFrame({'key': ['K0', 'K1', 'K3'], 'B': ['B0', 'B1', 'B3']})

# Merge df1 and df2
merged_df = pd.merge(df1, df2, on='key')

print(merged_df)

df3 = pd.DataFrame({'key1': ['K0', 'K1', 'K2'], 'A': ['A0', 'A1', 'A2']})
df4 = pd.DataFrame({'key2': ['K0', 'K1', 'K3'], 'B': ['B0', 'B1', 'B3']})

# Merge df3 and df4
merged_df2 = pd.merge(df3, df4, left_on='key1', right_on='key2')

print(merged_df2)

# Outer merge
outer_merged = pd.merge(df1, df2, on='key', how='outer')

print(outer_merged)

df5 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                    'key2': ['K0', 'K1', 'K0', 'K1'],
                    'A': ['A0', 'A1', 'A2', 'A3']})

df6 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                    'key2': ['K0', 'K0', 'K0', 'K0'],
                    'B': ['B0', 'B1', 'B2', 'B3']})

# Merge on multiple keys
multi_key_merged = pd.merge(df5, df6, on=['key1', 'key2'], how='outer')

print(multi_key_merged)
