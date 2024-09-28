def present_meal_plan(meal_plan_data_list):
    print(f"Your {meal_plan_data_list[0]} meals will be:")
    for n, item in enumerate(meal_plan_data_list[2]):
        print(f"{n + 1} : {item}")
    
    print("\nThis is what you have to buy in order to prepare:")
    for item in meal_plan_data_list[3]:
        print(item)