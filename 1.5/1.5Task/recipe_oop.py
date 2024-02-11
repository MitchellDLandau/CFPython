class Recipe:

    all_ingredients = set()

    def __init__(self, name, ingredients, cook_time):
        self.name = name
        self.ingredients = ingredients
        self.cook_time = cook_time
        self.difficulty = None

    def calc_difficulty(self):    
        num_ingred = len(self.ingredients)
        if self.cook_time <= 10 and num_ingred <= 4:
            return 'easy'
        elif self.cook_time <= 10 and num_ingred > 4:
            return "moderate"
        elif self.cook_time > 10 and num_ingred <= 4:
            return "intermediate"
        elif self.cook_time > 10 and num_ingred > 4:
            return "hard"

    def add_ingredients(self, *ingredients):         
        self.ingredients.extend(ingredients)
        self.update_all_ingredients
    
    def search_ingredients(self, ingredients):
        return ingredients in self.ingredients

    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            Recipe.all_ingredients.add(ingredient)
    
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_cook_time(self):
        return self.cook_time

    def set_cook_tiome(self, cook_time):
        self.cook_time = cook_time

    def get_ingredients(self):
        return self.ingredients
    
    def get_difficulty(self):
        if (type(self.difficulty) != str):
            self.calc_difficulty()
        return self.difficulty

    def __str__(self):
        return f"Recipe Name: {self.name}\nIngredients: {(self.ingredients)}\nCooking Time: {self.cook_time} minutes \nDifficulty: {self.get_difficulty()}\n" 
    
def recipe_search(data, search_term):
    print(f"Recipes containing {search_term} are: \n")
    for recipe in data:
        if recipe.search_ingredients(search_term):
            print(recipe)


#create recipes
tea = Recipe("Tea", ["Tea Leaves", "Sugar", "Water"], 5)
coffee = Recipe("Coffee", ["Coffee Powder", "Sugar", "Water"], 5)
cake = Recipe("Cake", ["Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk"], 50)
smoothie = Recipe("Banana Smoothie", ["Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes"], 5)
pizza = Recipe("Pizza", ["dough", "cheese", "Sauce"], 10)
pie = Recipe("pie", ["Crust", "Apples", "sugar", "cinnamon", "butter"], 115)
pork = Recipe("Pork", ["pork", "chili powder", "onion", "salt", "pepper"], 300)
#add all to a list
recipes_list = [tea, coffee, cake, smoothie, pizza, pie, pork]
#print all
for recipe in recipes_list:
    print(recipe)
#search for ingredient in recipes
for ingredient in ["Water", "Sugar", "Bananas"]:
    recipe_search(recipes_list, ingredient)