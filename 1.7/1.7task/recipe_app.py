import os
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

user = os.environ.get("username")
password = os.environ.get("password")
dbname = os.environ.get("database_name")
#I used password: password username: cf-python database: task_database
#connect to the database.
engine = create_engine("mysql+pymysql://{user}:{password}@localhost/{dbname}")
engine = create_engine("mysql+pymysql://cf-python:password@localhost/task_database")
#Base class for the table.
Base = declarative_base()
#Create session and initialize the database.
Session = sessionmaker(bind=engine)
session = Session()

#Creating the table for the recipes.
class Recipe(Base):
    __tablename__ = "practice_recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))
    #Representation of the recipe.
    def __repr__(self):
        return "Recipe ID: " + str(self.id) + " - " + self.name
    #Print the recipe.
    def __str__(self):
        return print(("-----"*10) + (f"\nRecipe ID: {self.id}\n Name: {self.name}\n Ingredients: {self.ingredients}\n Cooking Time: {self.cooking_time}\n Difficulty: {self.difficulty}\n"))
    #Calculate the difficulty of the recipe using parameters.
    def calc_difficulty(self):    
        number_of_ingredients = len(self.ingredients.split(", "))
        if self.cooking_time <= 10 and number_of_ingredients <= 4:
            self.difficulty = 'easy'
        elif self.cooking_time <= 10 and number_of_ingredients > 4:
            self.difficulty = "moderate"
        elif self.cooking_time > 10 and number_of_ingredients <= 4:
            self.difficulty = "intermediate"
        elif self.cooking_time > 10 and number_of_ingredients > 4:
            self.difficulty = "hard"
    #Return the ingredients as a list.
    def return_ingredients_as_list(self):
        if self.ingredients is None:
            return []
        else:
            self.ingredients.split(", ")

Base.metadata.create_all(engine)

#Definition for option 1 adding a recipe to the database. 
def option_1():
    name = ''
    cooking_time = ''
    #Collect name of recipe.
    while True:
        try:
            name =str(input("Enter the name of the recipe: "))
        except ValueError:
            print("That is not a valid name please try again.")
            continue
        if 1 > len(name):
            print("Names need some amount of characters.")
        elif len(name) >= 50:
            print("Names need to be less than 50 characters.")
        else:
            break
    #Collect cooking time for recipe.
    while True:
        try:
            cooking_time = int(input("Enter the cooking time for the recipe: "))
        except ValueError:
            print("That is not a valid number please try again.")
            continue
        if cooking_time < 0:
            print("Cooking time cannot be negative.")
        else:
            break

    #Collect ingredients for recipe.
    ingredients = []
    while True:
        try: 
            ingredient_count = int(input("How many ingredients are in the recipe? "))
        except ValueError:
            print("That is not a valid number.")
        if ingredient_count < 1:
            print("You need at least one ingredient.")
        elif ingredient_count > 40:
            print("You cannot have more than 40 ingredients.")
        else:
            break
    for i in range(ingredient_count):
        ingredient = input(f"Enter ingredient {i+1}: ")
        ingredients.append(ingredient)
    #Create a string of ingredients.
    ingredients_to_string = ", ".join(ingredients)
    #Create a new recipe object.
    recipe_to_add = Recipe(name=name, ingredients=ingredients_to_string, cooking_time=cooking_time)
    recipe_to_add.calc_difficulty()
    #commit to db
    session.add(recipe_to_add)
    session.commit()
    print(f"{name} has been added to your recipes list.")

def option_2():
    #View all recipes.
    print(("-----"*5) + ("Here are all your recipes:") + ("-----"*5))
    #Query the database for all recipes.
    recipes = session.query(Recipe).all()
    #Print all recipes.
    if recipes == []:
        print("There are no recipes in your list yet. Please add some.")
        main_menu() 
        # return None 
        #Unsure if I need the line above or not.
    else:
        for recipe in recipes:
            print(Recipe.__str__(recipe))
    print("-----"*10)

#Search for recipes that use a specific ingredient
def option_3():
    print("-----"*10)
    #Query the database for all recipes.
    recipes = session.query(Recipe).count()
    #return to main menu if no recipes are found.
    if recipes == 0:
        print("There are no recipes in your list yet. Please add some.")
        # main_menu()
    else:
        #Get all recipe ingredients.
        results =  session.query(Recipe.ingredients).all()
        all_ingredients = set()
        #split up all ingredients and add them to a list.
        for row in results:
            ingredients = row[0].split(", ")
            all_ingredients.update(ingredients)
        #Sort, number, and list the ingredients.             
        sorted_ingredients = sorted(all_ingredients)
        for index, ingredient in enumerate(sorted_ingredients):
            print(f"{index + 1}: {ingredient}")
        print("-----"*10)
        try:
            #request the ingredient to search for.
            ingredient_entered = int(input("Enter the number of the ingredient you would like to search for\nIf there is more than one seperate them by a coma: ").split(", "))
            #Loop over all entered ingredients.
            for ingredient_n in ingredient_numbers:
                ingredient_index = int(ingredient_n) - 1
                if 0 <= ingredient_index < len(sorted_ingredients):
                    search_ingredient = sorted_ingredients[ingredient_index]
                    print(f"Recipes that contain {search_ingredient}: ")
                    #Query the database for all recipes that contain the ingredient and print the recipe.
                    recipes = session.query(Recipe).filter(Recipe.ingredients.like(f"%{search_ingredient}%")).all()
                    for recipe in recipes:
                        print(Recipe.__str__(recipe))
                else :
                    print("Invalid ingredient number. Please try again.")
                    option_3()     
        except ValueError:
            print("That is not a valid number.")
            option_3()
    print("-----"*10)