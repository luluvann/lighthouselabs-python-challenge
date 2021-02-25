# Day 9 - Fillna and statistics

    import pandas as pd
    df = pd.read_csv('data9.csv')
    print(df.head(3))

    #How many entries NaN in each column
    print(df.info())

    #Fill the NaN entries with the median for each column
    median_milk = df['Monthly milk production: pounds per cow'].median()
    df['Monthly milk production: pounds per cow'] = df['Monthly milk production: pounds per cow'].fillna(value = median_milk)

    #What is the average for monthly milk production?
    mean_milk = df['Monthly milk production: pounds per cow'].mean()
    print(f'Mean milk prod: {mean_milk}')

    #What is the standard deviation for monthly milk production?
    std_milk = df['Monthly milk production: pounds per cow'].std()
    print(f'Standard deviation milk prod: {std_milk}')

    #What is the average number of cows used?
    median_num_cow = df['Number of Cows'].median()

    df['Number of Cows'] = df['Number of Cows'].fillna(value = median_num_cow)

    mean_num_cow = df['Number of Cows'].mean()

    print(f'Mean number of Cows: {mean_num_cow}')