# Day 13

import pandas as pd
wine_df = pd.read_csv('day13.csv')


#Q1 - Which wines had a quality of 8 or higher and a residual sugar level above 5?
filter_wine = wine_df['residual sugar'] > 5.00

filtered_df = wine_df[filter_wine]

new_df = filtered_df.sort_values(by=['quality','residual sugar'], ascending = False)

print(new_df)
print("Wine 0 and 1")

#Q2 - How many wines in total had a quality of 5 and 4 and a citric acid level below 0.4?
filter_wine_2 = wine_df['citric acid'] < 0.4

filtered_df_2 = wine_df[filter_wine_2]

new_df_2 = filtered_df_2['quality'].value_counts()

print(new_df_2)

print("9 wines have a quality of 5(7) and 4(2) and a citric acid level below 0.4")