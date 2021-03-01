# Day 11 - Find the average cost in Albany in 2017

import pandas as pd

df = pd.read_csv('day11.csv', index_col = 0)

filtered_df = df.loc[df.Region=='Albany']
avg_cost_per_year = filtered_df.groupby(["Year"]).mean()

print(avg_cost_per_year)