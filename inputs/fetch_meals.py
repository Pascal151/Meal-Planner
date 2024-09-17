available_meals = {
    "Tomato soup and cheese bread": [(500, "g", "tomatoes"), (2, "", "onions"), (3, "", "garlic kloves"), (30, "ml", "olive oil"), (4, "slices", "bread"), (4, "sclices", "gouda cheese")], #TODO: optional ingridients
    "Aglio olio": [(3, "", "garlic kloves"), (30, "ml", "olive oil"), (350, "g", "pasta"), (None, "", "parsley")],
}

def fetch_available_meals():
    return available_meals