import pandas as pd
import numpy as np


df1 = pd.read_csv('15-16_NBA_player_stats.csv')
df2 = pd.read_csv('16-17_NBA player_stats.csv')
df3 = pd.read_csv('17-18_NBA_player_stats.csv')
df4 = pd.read_csv('18-19_NBA_player_stats.csv')

# Creation of Pd DataFrames to view NBA Data

stats_15_16 = pd.DataFrame(df1)
stats_16_17 = pd.DataFrame(df2)
stats_17_18 = pd.DataFrame(df3)
stats_18_19 = pd.DataFrame(df4)

stats_15_16


# stats.iloc[:3,:3]

# ------------------------------------------------

counts = df1['Player'].value_counts()

# Show all duplicates in dataset

df1[df1['Player'].isin(counts.index[counts > 1])]

# ------------------------------------------------

results = stats_15_16.drop_duplicates(['Player'], keep = 'first')

# filtered out duplicate players based on highest G value

results

# TODO: Decide which columns to keep and which to drop 
#   - Once decided, create list of to_drop columns and use pd.drop(list, inplace=True, axis=1) function
