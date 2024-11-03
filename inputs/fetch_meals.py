import nltk

english_stemming = nltk.stem.SnowballStemmer('english')

available_meals = {
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

# Lemmatizing the dictionary
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')

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