# Day 12 - in which year or years did both conventional and organic avocados have had average prices above $2?

import pandas as pd

df = pd.read_csv('day12.csv', index_col = 0)

user_filter = df['AveragePrice'] >= 2

filtered_df = df[user_filter]

count_prices = filtered_df.groupby(['year','type']).count()

print(count_prices)

print("In 2016, both conventional and organic avocados have had average prices above 2$")