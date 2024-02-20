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
        if self.ingredients is []:
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
    try:
        if recipes == []:
            print("There are no recipes in your list yet. Please add some.")
            main_menu() 
        else:
            for recipe in recipes:
                print(Recipe.__str__(recipe))
        print("-----"*10)
        menu = input("When you are ready to return to the main menu press enter.")
        if menu == "":
            main_menu()
    except ValueError:
        print("That is not a valid input. Please try again.")
        option_2()


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
            ingredient_entered = input("Enter the number of the ingredient you would like to search for\nIf there is more than one seperate them by a coma: ").split(", ")
            #Loop over all entered ingredients.
            for ingredient_n in ingredient_entered:
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
            print("That is not a valid number. Please try again.")
            option_3()
    print("-----"*10)

def option_4():
    print("-----"*10)
    #Query the database for all recipes.
    recipes = session.query(Recipe).count()
    #return to main menu if no recipes are found.
    if recipes == 0:
        print("There are no recipes in your list yet. Please add some.")
        main_menu()
    else:
        #Get all recipe names.
        print("These are your current recipes: ")
        results = session.query(Recipe.id, Recipe.name).all()
        id_list = []
        for recipe in results:
            id_list.append(recipe[0])
            print(f"Recipe id: {recipe[0]} Recipe name: {recipe[1]}")
        print("If you do not wish to edit any item type menu")
        try:
            #Ask for the id of the recipe to upddate.
            recipe_id = (input("Enter the id of the recipe you would like to edit: "))
            if recipe_id == "menu":
                main_menu()
            recipe_id = int(recipe_id)  # Convert to integer
            if recipe_id not in id_list:
                print("Invalid recipe number. Please try again.")
                option_4()
            #Get the recipe to update.
            recipe_to_edit = session.query(Recipe).filter(Recipe.id == recipe_id).first()
            #Print the recipe to update.
            print(("-----"*10) + (f"\nRecipe ID: {recipe_to_edit.id}\n1.) Name: {recipe_to_edit.name}\n2.) Ingredients: {recipe_to_edit.ingredients}\n3.) Cooking Time: {recipe_to_edit.cooking_time}\nDifficulty: {recipe_to_edit.difficulty}\tDifficulty is not editable\n4.) If you do not wish to edit any item select 4"))
            print("-----"*10)
            edit_choice = input("Enter the number of the field you would like to edit: ")
            print("-----"*10)

            if edit_choice == "1":
                #Ask for the new name of the recipe.
                new_name = input(f"Enter the new name for {recipe_to_edit.name}: ")
                recipe_to_edit.name = new_name
                #Update the recipe in the database.
                session.query(Recipe).filter(Recipe.id == recipe_id).update({Recipe.name: new_name})
                session.commit()
                print(f"The name of the recipe has been changed to {new_name}.")
            elif edit_choice == "2":
                ingredients = []
                #Ask how many ingredients are in the recipe.
                while True:
                    try: 
                        ingredient_count = int(input(f"How many ingredients are in {recipe_to_edit.name}?"))
                        print("-----"*10)
                    except ValueError:
                        print("That is not a valid number.")
                    if ingredient_count < 1:
                        print("You need at least one ingredient.")
                    elif ingredient_count > 40:
                        print("You cannot have more than 40 ingredients.")
                    else:
                        break
                #Ask for each ingredient.
                for i in range(ingredient_count):
                    ingredient = input(f"Enter ingredient {i+1}: ")
                    ingredients.append(ingredient)  # This line should be inside the loop
                    # Create a string of ingredients.
                    ingredients_to_string = ", ".join(ingredients)
                    # Create a new recipe object.
                    recipe_to_edit.ingredients = ingredients_to_string
                    print(f"Curent entered ingredients: {ingredients_to_string}")
                    # Calculate the difficulty of the recipe.
                    Recipe.calc_difficulty(recipe_to_edit)
                    # Update the recipe in the database.
                    session.query(Recipe).filter(Recipe.id == recipe_id).update(
                        {Recipe.ingredients: ingredients_to_string, 
                        Recipe.difficulty: recipe_to_edit.difficulty}
                    )

                session.commit()
                print(f"The ingredients for the recipe have been updated to {ingredients_to_string}.")
            #Ask for the new cooking time of the recipe.
            elif edit_choice == "3":
                new_cooking_time = int(input("Enter the new cooking time for the recipe: "))
                recipe_to_edit.cooking_time = new_cooking_time
                #Calculate the difficulty of the recipe.
                Recipe.calc_difficulty(recipe_to_edit)
                session.query(Recipe).filter(Recipe.id == recipe_id).update(
                    {Recipe.cooking_time: new_cooking_time, 
                     Recipe.difficulty: recipe_to_edit.difficulty}
                    )
                #Update the recipe in the database.
                session.commit()
                print(f"The cooking time for the recipe has been changed to {new_cooking_time}.")
            #If the user does not want to update anything.
            elif edit_choice == "4":
                print("No updates will be recorded.")
                main_menu()
            #Error handling for invalid input.    
            else:
                print("Invalid choice. Please try again.")
                option_4()
        #Error handling for invalid input.
        except ValueError:
            print("That is not a valid number. Please try again.")
            option_4()
        finally: main_menu()

def option_5():
    print("-----"*10)
    #Query the database for all recipes.
    recipes = session.query(Recipe).count()
    #return to main menu if no recipes are found.
    if recipes == 0:
        print("There are no recipes in your list yet. Please add some.")
        main_menu()
    else:
        #Get all recipe names.
        print("These are your current recipes: ")
        results = session.query(Recipe.id, Recipe.name).all()
        id_list = []
        for recipe in results:
            id_list.append(recipe[0])
            print(f"Recipe id: {recipe[0]} Recipe name: {recipe[1]}")
        print("If you do not wish to delete any item type menu")
        try:
            # Ask for the id of the recipe to delete.
            recipe_id = input("Enter the id of the recipe you would like to delete: ")
            if recipe_id == "menu":
                main_menu()
            recipe_id = int(recipe_id)  # Convert to integer
            if recipe_id not in id_list:
                print("Invalid recipe number. Please try again.")
                option_5()
            # Get the recipe to delete.
            recipe_to_delete = session.query(Recipe).filter(Recipe.id == recipe_id).first()
            #Request confirmation to delete the recipe.
            print("Are you sure you wish to delete this recipe?")
            print(Recipe.__str__(recipe_to_delete))
            delete_choice = input("Enter 'yes' to delete or 'no' to cancel: ")
            #delete the recipe from the database.
            if delete_choice == "yes":
                session.delete(recipe_to_delete)
                session.commit()
                print(f"{recipe_to_delete.name} has been deleted.")
            #If the user does not want to delete the recipe.
            elif delete_choice == "no":
                print("No recipes will be deleted.")
                main_menu()
        except ValueError:
            print("That is not a valid number. Please try again.")
            option_5()
        finally:
            main_menu()

def main_menu():
    choice = ""
    #Options for the user to choose from.
    while(choice != "quit"):
        print("-------------------------------------------------------------------------------")
        print("What would you like to do?")
        print("1. Add a recipe to the database.")
        print("2. View all recipes in the database.")
        print("3. Search for a recipe that uses a specific ingredient.")
        print("4. Update a recipe in the database.")
        print("5. Delete a recipe from the database.")
        print("Type 'quit' to exit the program.")
        print("-------------------------------------------------------------------------------")
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            option_1()
        elif choice == "2":
            option_2()
        elif choice == "3":
            option_3()
        elif choice == "4":
            option_4()
        elif choice == "5":
            option_5()
        elif choice == "quit":
            session.close()
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")