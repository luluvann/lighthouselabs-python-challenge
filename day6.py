# Day 6 - use Panda to calculate stats

import random 
import pandas as pd

random.seed(34)

hole_sizes = [random.randint(1, i) for i in range(1, 101)]
random.shuffle(hole_sizes)

    # hole sizes in mm

    series = pd.Series(hole_sizes)

    #Small (less than 20 mm)	$1.30
    #Medium (above or equal to 20 mm AND less than 70mm)	$1.60
    #Large (above or equal to 70 mm)	$2.10

# Solution

    # what is the hole sizes mean ?
    print(series.mean())

    # What is the unit cost mean
    cost = []

    for i in range(len(hole_sizes)):
    if hole_sizes[i] < 20:
        cost.append(1.3)
    elif hole_sizes[i] < 70:
        cost.append(1.6)
    else:  cost.append(2.1)

    series_cost = pd.Series(cost)

    print(series_cost.mean())

    # What is the total cost

    total_cost = 0

    for i in range(len(hole_sizes)):
    if hole_sizes[i] < 20:
        total_cost += 1.3
    elif hole_sizes[i] < 70:
        total_cost += 1.6
    else:  total_cost += 2.1

    print(total_cost)
