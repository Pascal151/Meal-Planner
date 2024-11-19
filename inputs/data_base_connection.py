import psycopg2

meals = {
    "Tomato soup and cheese bread": [(500, "g", "tomatoes"), (2, "", "onions"), (3, "", "garlic cloves"), (30, "ml", "olive oil"), (4, "slices", "bread"), (4, "sclices", "gouda cheese")], #TODO: optional ingridients
    "Aglio olio": [(3, "", "garlic cloves"), (30, "ml", "olive oil"), (350, "g", "pasta"), (None, "", "parsley")],
    "Chicken Caesar Salad": [(200, "g", "chicken breast"), (100, "g", "romaine lettuce"), (50, "g", "croutons"), (50, "g", "parmesan cheese"), (30, "ml", "Caesar dressing"), (2, "", "boiled eggs"), (20, "ml", "olive oil")],
    "Spaghetti Bolognese": [(400, "g", "ground beef"), (500, "g", "spaghetti"), (1, "can", "tomato sauce"), (1, "", "onion"), (2, "", "garlic cloves"), (30, "ml", "olive oil"), (None, "", "fresh basil")],
    "Vegetable Stir Fry": [(200, "g", "broccoli"), (1, "", "carrot"), (1, "", "bell pepper"), (100, "g", "snap peas"), (2, "", "garlic cloves"), (30, "ml", "soy sauce"), (10, "ml", "sesame oil"), (None, "", "green onions")],
    "Beef Tacos": [(300, "g", "ground beef"), (6, "", "taco shells"), (100, "g", "cheddar cheese"), (50, "g", "lettuce"), (2, "", "tomatoes"), (30, "ml", "sour cream"), (None, "", "taco seasoning")],
    "Grilled Salmon with Asparagus": [(200, "g", "salmon fillet"), (150, "g", "asparagus"), (1, "", "lemon"), (30, "ml", "olive oil"), (None, "", "fresh dill"), (None, "", "salt and pepper")],
    "Mushroom Risotto": [(300, "g", "arborio rice"), (200, "g", "mushrooms"), (1, "", "onion"), (2, "", "garlic cloves"), (50, "g", "parmesan cheese"), (30, "ml", "olive oil"), (750, "ml", "vegetable broth")],
    "Caprese Salad": [(2, "", "tomatoes"), (150, "g", "mozzarella cheese"), (30, "ml", "olive oil"), (None, "", "basil leaves"), (None, "", "balsamic glaze")],
    "Greek Salad": [(2, "", "tomatoes"), (1, "", "cucumber"), (1, "", "red onion"), (100, "g", "feta cheese"), (50, "g", "kalamata olives"), (30, "ml", "olive oil"), (10, "ml", "red wine vinegar"), (None, "", "oregano")],
    "Shakshuka": [(1, "", "onion"), (1, "", "bell pepper"), (3, "", "garlic cloves"), (400, "g", "tomato puree"), (4, "", "eggs"), (30, "ml", "olive oil"), (None, "", "cumin"), (None, "", "paprika"), (None, "", "parsley")],
    "Grilled Lamb Chops with Tzatziki": [(4, "", "lamb chops"), (150, "g", "yogurt"), (1, "", "cucumber"), (2, "", "garlic cloves"), (10, "ml", "lemon juice"), (30, "ml", "olive oil"), (None, "", "fresh mint"), (None, "", "dill")],
    "Spanakopita": [(500, "g", "spinach"), (200, "g", "feta cheese"), (1, "", "onion"), (2, "", "garlic cloves"), (1, "", "egg"), (8, "", "phyllo dough sheets"), (50, "g", "butter"), (30, "ml", "olive oil")],
    "Falafel Wrap": [(200, "g", "chickpeas"), (1, "", "onion"), (3, "", "garlic cloves"), (30, "g", "flour"), (10, "g", "parsley"), (30, "ml", "olive oil"), (4, "", "tortilla wraps"), (50, "g", "tahini sauce"), (None, "", "lettuce leaves"), (None, "", "tomato slices")],
    "Hummus and Pita Bread": [(200, "g", "chickpeas"), (2, "", "garlic cloves"), (30, "ml", "tahini"), (30, "ml", "lemon juice"), (50, "ml", "olive oil"), (4, "", "pita bread"), (None, "", "paprika"), (None, "", "cumin")],
    "Tabbouleh": [(100, "g", "bulgur wheat"), (2, "", "tomatoes"), (1, "", "cucumber"), (30, "g", "parsley"), (10, "g", "mint"), (30, "ml", "olive oil"), (10, "ml", "lemon juice"), (None, "", "green onions")],
    "Stuffed Bell Peppers": [(4, "", "bell peppers"), (200, "g", "ground beef"), (100, "g", "rice"), (1, "", "onion"), (2, "", "garlic cloves"), (400, "g", "tomato sauce"), (30, "ml", "olive oil"), (50, "g", "feta cheese"), (None, "", "parsley")],
    "Mediterranean Grilled Vegetables": [(1, "", "zucchini"), (1, "", "eggplant"), (1, "", "bell pepper"), (1, "", "red onion"), (30, "ml", "olive oil"), (10, "ml", "balsamic vinegar"), (None, "", "thyme"), (None, "", "oregano")],
    "Seafood Paella": [(200, "g", "shrimp"), (200, "g", "mussels"), (300, "g", "paella rice"), (1, "", "onion"), (3, "", "garlic cloves"), (1, "l", "fish stock"), (100, "g", "peas"), (1, "", "bell pepper"), (30, "ml", "olive oil"), (None, "", "saffron")]
}

try:
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        dbname="Mealplanner",
        user="postgres",
        password="357654",
        host="localhost",
        port="7531"
    )
    cursor = conn.cursor()

    # Create table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Meals (
        meal_id SERIAL PRIMARY KEY,
        meal_name TEXT,
        quantity INTEGER,
        unit TEXT,
        ingredient TEXT
    );
    """
    cursor.execute(create_table_query)
    conn.commit()

    # Insert data into the table
    insert_query = """
    INSERT INTO Meals (meal_name, quantity, unit, ingredient) 
    VALUES (%s, %s, %s, %s)
    """

    # Insert each ingredient into the Meal_Ingredients table
    for meal_name, ingredients_list in meals.items():
        for ingredient in ingredients_list:
            quantity, unit, ingredient_name = ingredient
            cursor.execute(insert_query, (meal_name, quantity, unit, ingredient_name))

    # Commit all insertions at once
    conn.commit()
    print("Data inserted successfully!")

except Exception as e:
    print("Error:", e)

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
