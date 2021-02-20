# Day 4 - Buy bulk at wholesale price or buy at retail price ?

item_list = ['Oak Wood', 'Blue Paint', 'White Paint', 'Paint Finish']

quantity_list = [600,150,15,165]

wholesale_bulk_list = [7000, 1000, 1000, 800]

retail_price_list = [12.99, 8.99, 9.99, 3.99]


# Solution

choice = []

for i in range(len(item_list)): 
    if amount_list[i]*retail_price[i] > wholesale_price_list[i]:
      choice.append(f'{item_list[i]}: Yes')
    else :
      choice.append(f'{item_list[i]}: No')

print(f'Buy Wholesale ? {choice}')

    # Output: Buy Wholesale ? ['Oak Wood: Yes', 'Blue Paint: Yes', 'White Paint: No', 'Paint Finish: No']
