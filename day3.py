# Day 3 - Generate a paint shopping list based on the new requirements

    # Requirements
    old_blueprint = {
        "Kitchen": ['Dirty', 'Oak', "Damaged", "Green"],
        "Dining Room": ['Dirty', 'Pine', 'Good Condition', 'Grey'],
        "Living Room": ['Dirty', 'Oak', 'Damaged', 'Red'],
        "Bedroom" : ["Clean", 'Mahogany', 'Good Condition', 'Green'],
        "Bathroom": ["Dirty", 'White Tile', 'Good Condition','White'],
        "Shed"    : ['Dirty', "Cherry", "Damaged", "Un-painted"]
    }

    old_shopping_list = ['20 x Oak plank', '20 x Oak Plank', '20 x Cherry Plank', 'White Paint', 'White Paint', 'White Paint']

    # New requirements
        # Replace the Oak wood by Maple wood
        # Paint the kitchen in blue instead of white
    
    # Solution
        new_shopping_list = ['20 x Maple plank', '20 x Maple plank', '20 x Cherry Plank','Blue Paint', 'White Paint', 'White Paint']

        paint_list = new_shopping_list[3:]

        print(paint_list)



