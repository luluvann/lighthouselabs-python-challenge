# Day 2 - What is the difference between the total amount of groceries in the city vs. groceries in the country, as a percentage of country grocery total amount?

    # Grocery List (19 items)
    grocery_list = ['Bananas', 'Clementines', 'Baguette', 'Oat Milk', 'Olive Oil', 'Coffee Beans',
                    'Chocolate Bar', 'Brocolli', 'Eggplant', 'Chickpeas', 'Lentils', 'Tomatoes',
                    'Pasta', 'Rice', 'Yogurt', 'Blueberries', 'Onions', 'Garlic', 'Truffles']

    # City Price
    city_price = [6.49, 4.99, 4.39, 4.29, 11.99, 17.99,          
                3.49, 3.99, 1.10, 1.99, 2.99, 4.68,            
                1.59, 8.99, 3.49, 6.99, 2.99, 1.98, 14.99]

    # Country Price
    country_price = [4.49, 4.12, 3.42, 6.99, 7.99, 14.99,              
                    2.99, 2.49, 0.99, 1.49, 2.49, 1.99,              
                    1.59, 6.99, 3.89, 4.99, 1.69, 1.87, 11.49]

# Solution

city_total = sum(city_price)
country_total = sum(country_price)

difference_in_percent = round(((city_total - country_total) / country_total * 100),2)

print(f'The grocery expenses in the city are {difference_in_percent}% higher than in the country')