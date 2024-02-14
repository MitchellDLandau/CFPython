import os
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="cf-python",
    passwd="password"
)

cursor = conn.cursor()
#Use the database.
cursor.execute("USE task_database")
#Creation of the database if it does not exist.
cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")
#Creation of the table if it does not exist.
cursor.execute('''CREATE TABLE IF NOT EXISTS recipes(
    item_id             INT,
    name                VARCHAR(50),
    ingredients         VARCHAR(250),
    cooking_time        INT,
    difficulty          VARCHAR(20)
    )''')

#Definition for option 1 adding a recipe to the database. 
def option_1():
    print("-------------------------------------------------------------------------------")
    #Collect necessary information for the recipe.
    a = input("Name of the recipe: ")
    b = int(input("Cook time for the recipe: "))
    c = input("Ingredients in recipe separated by a comma: ").split(", ")
    d = calc_difficulty(b, c)
    # recipe = {'name': a, 'cooking_time': b, 'ingredients': c, 'difficulty': d}

    ingredients_to_string = ', '.join(c)
#Values to be inserted into the database.
    sql = f"INSERT INTO recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)"
    val = (a, ingredients_to_string, b, d)
#Insert the recipe into the database.
    cursor.execute(sql, val)
    
    conn.commit()
    print(f"{a} has been added to the list.")
    # conn.close()

    #Calculate the difficulty of the recipe using parameters.
def calc_difficulty(b, c):    
    if b <= 10 and len(c) <= 4:
        return 'easy'
    elif b <= 10 and len(c) > 4:
        return "moderate"
    elif b > 10 and len(c) <= 4:
        return "intermediate"
    elif b > 10 and len(c) > 4:
        return "hard"

#Definition for option 2 searching for a recipe that uses a specific ingredient.
def option_2():
    print("-------------------------------------------------------------------------------")
    #grab all ingredients.
    cursor.execute("SELECT ingredients FROM recipes")
    results = cursor.fetchall()
    #splitting all ingredients into a set.
    all_ingredients = set()
    for row in results:
        ingredients = row[0].split(", ")
        for ingredient in ingredients:
            all_ingredients.add(ingredient)
    #sorting the list of ingredients found.
    sorted_ingredients = sorted(all_ingredients)
    #printing the list of ingredients sorted.
    for index, ingredient in enumerate(sorted_ingredients):
        print(index + 1, ingredient)
    #asking the user for the ingredient they want to search for.
    print("-------------------------------------------------------------------------------")
    try:
        number = int(input("Type the number for the ingredient you would like recipes it is used in?"))
        search_ingredient = sorted_ingredients[number - 1]
        print(f"search_ingredient: {search_ingredient}")

        cursor.execute("SELECT * FROM recipes WHERE ingredients LIKE %s", (f"%{search_ingredient}%",))
        results = cursor.fetchall()
        for recipe in results:
            print(f"------------------{recipe[1]} uses {search_ingredient}---------------------")
            display_recipe(recipe)
            return
    except ValueError:
        print("Numbers are the only allowed characters.")
        option_2()
    except IndexError:
        print("Invalid choice. Please try again.")
        option_2()
    else:
        print("Invalid choice. Please try again.")
        option_2()




    if number != int:
        print("Numbers are the only allowed characters.")
        print("-----------------------------------Please try again--------------------------------------------")
        option_2()
    elif number != index:
        print("Invalid choice. Please try again.")
        option_2()
    else:
        search_ingredient = sorted_ingredients[number - 1]
        print(f"search_ingredient: {search_ingredient}")

        cursor.execute("SELECT * FROM recipes WHERE ingredients LIKE %s", (f"%{search_ingredient}%",))
        results = cursor.fetchall()
        for recipe in results:
            print(f"------------------{recipe[1]} uses {search_ingredient}---------------------")
            display_recipe(recipe)

#Definition for option 3 updating a recipe in the database.
def option_3():
    print("-------------------------------------------------------------------------------")
    cursor.execute("SELECT * FROM recipes")
    results = cursor.fetchall()
    #print recipe ID and name for user to choose from.
    for recipe in results:
        print(f"ID: {recipe[0]}, Name: {recipe[1]}")
    #Loop to ensure the user selects a valid recipe ID.
    while True:
        try:
            recipe_id = int(input("Type the ID for the recipe you would like to update?"))
            if any(recipe_id == recipe[0] for recipe in results):
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid ID.")
    #Ask the user which part of the recipe they would like to update.
    print("-------------------------------------------------------------------------------")
    recipe_name = [recipe[1] for recipe in results if recipe[0] == recipe_id][0]
    print(f"Which part of your {recipe_name} recipe would you like to update?")
    print("1. Name")
    print("2. Ingredients")
    print("3. Cooking Time")
    print("4. No update needed.")
    #options to update what the user would like to update or exit.
    update_choice = int(input("Enter the number of your choice: "))
    print("-------------------------------------------------------------------------------")
    if update_choice == 1:
        new_name = input(f"Enter the new name for the recipe previously called {recipe_name}: ")
        cursor.execute("UPDATE recipes SET name = %s WHERE item_id = %s", (new_name, recipe_id))
        conn.commit()
        print(f"{new_name} has been updated.")
    elif update_choice == 2:
        new_ingredients = input(f"Enter the new ingredients for {recipe_name} separated by a comma: ").split(", ")
        new_ingredients_to_string = ', '.join(new_ingredients)
        cursor.execute("UPDATE recipes SET ingredients = %s WHERE item_id = %s", (new_ingredients_to_string, recipe_id))
        conn.commit()
        print(f"{recipe_name} has been updated.")
    elif update_choice == 3:
        new_cooking_time = int(input(f"Enter the new cooking time for {recipe_name}: "))
        cursor.execute("UPDATE recipes SET cooking_time = %s WHERE item_id = %s", (new_cooking_time, recipe_id))
        conn.commit()
        print(f"{recipe_name} has been updated.")
    elif update_choice == 4:
        print(f"No update needed for {recipe_name}.")
    else:
        print("Invalid choice. Please try again.")

#Definition for option 4 deleting a recipe from the database.
def option_4():
    print("-------------------------------------------------------------------------------")
    cursor.execute("SELECT * FROM recipes")
    results = cursor.fetchall()
    #print recipe ID and name for user to choose from.
    for recipe in results:
        print(f"ID: {recipe[0]}, Name: {recipe[1]}")

    delete_ID = int(input("Type the ID for the Recipe you wish to delete: "))
    cursor.execute("DELETE FROM recipes WHERE item_id = %s", (delete_ID,))
    recipe_name = [recipe[1] for recipe in results if recipe[0] == delete_ID]
    print(f"{recipe_name} has been deleted.")

#Definition to close the application and exit. 
def option_5():
    conn.close()
    exit()

def display_recipe(recipe):
    print("Recipe: " + recipe[1])
    print("Cooking Time: " + str(recipe[3]) + " minutes")
    print("Difficulty level: " + recipe[4])
    print("Ingredients: ")
    for position, ingredient in enumerate(recipe[2].split(', ')):
        print(str(position + 1) + ", " + ingredient)

#Definition for the main menu of the application.
def main_menu():
    choice = ""
    while(choice != "quit"):
        print("-------------------------------------------------------------------------------")
        print("What would you like to do?")
        print("1. Add a recipe to the database.")
        print("2. Search for a recipe that uses a specific ingredient.")
        print("3. Update a recipe in the database.")
        print("4. Delete a recipe from the database.")
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
        elif choice == "quit":
            option_5()
            print("Goodbye!")
        else:
            print("Invalid choice. Please try again.")

#pull all recipes from the database
cursor.execute("SELECT * FROM recipes")

results = cursor.fetchall()
for row in results:
     print("ID: ", row[0])
     print("Name: ", row[1])
     print("ingredients: ", row[2])
     print("cooking_time", row[3])
     print("difficulty:", row[4])
     print()

     cursor.execute("ALTER TABLE recipes MODIFY COLUMN item_id INT AUTO_INCREMENT")