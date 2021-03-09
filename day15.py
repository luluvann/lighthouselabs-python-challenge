# Day 15 - Data Vizualization

import numpy as np
import matplotlib.pyplot as plt

seeds = {
    'Vegetable' : ['Carrots', 'Tomatoes', 'Potatoes', 'Eggplant', 'Cucumbers'],
    'Seeds_Count' : [300,10,90,100,15],
    'Each_Seed_Produces': [1,140,10,5, 90]
}

items = seeds["Vegetable"]
a = np.array(seeds["Seeds_Count"])
b = np.array(seeds["Each_Seed_Produces"])
production = a*b

plt.figure()
plt.bar(x = items, height = production)
plt.show()