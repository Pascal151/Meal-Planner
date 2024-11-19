import psycopg2
import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="Mealplanner",
    user="postgres",
    password="357654",
    host="localhost",
    port="7531"
)
cursor = conn.cursor()

# Fetch all rows from the Meals table
cursor.execute("SELECT meal_name, quantity, unit, ingredient FROM Meals ORDER BY meal_name, ingredient;")
rows = cursor.fetchall()

# Initialize an empty dictionary to hold the meals data
available_meals = {}

# Group ingredients by meal_name
for row in rows:
    meal_name, quantity, unit, ingredient = row
    if meal_name not in available_meals:
        available_meals[meal_name] = []
    # Append each ingredient as a tuple (quantity, unit, ingredient_name)
    available_meals[meal_name].append((quantity, unit, ingredient))

# Close the cursor and connection
cursor.close()
conn.close()

# Lemmatizing the dictionary
lemmatizer = WordNetLemmatizer()

def lemmatize_ingredient(word):
    return lemmatizer.lemmatize(word, pos=wordnet.NOUN)

for key, array in available_meals.items():
    for i, (a, b, c) in enumerate(array):
        if b != "":
            stemmed_c = lemmatize_ingredient(c)
            array[i] = (a, b, stemmed_c)

def fetch_available_meals():
    return available_meals
