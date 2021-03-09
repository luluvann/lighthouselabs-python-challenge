# Day 16 - Boxplot
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("day16.csv")

df.head(2)

plt.figure()
plt.boxplot(df['num_pages'], vert = False)
plt.show()