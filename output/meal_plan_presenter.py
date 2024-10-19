import pandas as pd
from typing import Tuple, List

TupleType = Tuple[int, str, str] #TODO: test if tuple typing is really needed.

def present_meal_plan(meal_plan_data_list):
    print(f"Your {meal_plan_data_list[0]} meals will be:")
    for n, item in enumerate(meal_plan_data_list[2]):
        print(f"{n + 1} : {item}")
    
    print("Grocery shopping list:")
    ingredients_tuple_list: List[TupleType] = [tup for sublist in meal_plan_data_list[3] for tup in sublist]
    grocery_shopping_list = (
        pd.DataFrame(ingredients_tuple_list, columns=['amount', 'metric', 'ingredient'])
        .dropna(subset=['amount', 'metric', 'ingredient'])
        .astype({'amount': 'int32', 'metric': 'string', 'ingredient': 'string'})
    )

    # Normalize ingredient names by removing trailing 's'
    grocery_shopping_list['normalized'] = grocery_shopping_list['ingredient'].str.rstrip('s')

    # aggregate the ingredients
    aggregated_grocery_shopping_list = (
        grocery_shopping_list
        .groupby(['metric', 'normalized'], as_index=False).agg({'amount': 'sum'})
    )

    # Strip awas the 's' when amount is 1
    aggregated_grocery_shopping_list['ingredient'] = aggregated_grocery_shopping_list.apply(
        lambda row: row['normalized'] 
        if row['metric'] == 'ml' 
        or row['metric'] == 'g' 
        or row['amount'] == 1 
        else row['normalized'] + 's', axis=1
    )
    
    aggregated_grocery_shopping_list = aggregated_grocery_shopping_list.drop(columns=['normalized'])

    return(aggregated_grocery_shopping_list.sort_values(by='ingredient'))