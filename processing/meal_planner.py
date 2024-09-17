import random

def get_meal_plan_data_list(available_meals, user_specifications):
    amount_of_meals = user_specifications * 2
    meal_selection = random.choices(list(available_meals.items()), k=amount_of_meals)
    meal_plan = [tup[0] for tup in meal_selection]
    grocery_shopping_list = [tup[1] for tup in meal_selection]

    return [amount_of_meals, meal_selection, meal_plan, grocery_shopping_list]