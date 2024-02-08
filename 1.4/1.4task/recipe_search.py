import pickle

def display_recipe(recipe):
    print("Recipe: " + recipe['name'])
    print("Cooking Time: " + str(recipe['cooking_time']) + " minutes")
    print("Difficulty level: " + recipe['difficulty'])
    print("Ingredients: ")
    for position, ingredient in enumerate(recipe['ingredients']):
        print(str(position + 1) + ", " + ingredient)

def search_ingredient(data):
    ingredients = enumerate(data['ingredients_list'])
    ingredients_numbered = list(ingredients)

    for ingredient in ingredients_numbered:
        print(ingredient[0], ingredient[1])

    try: 
        i = int(input("Which ingredient would you like recipes it is used in?"))
        ingredient_searched = ingredients_numbered[i][1]
        print('searching for recipes that use ' + ingredient_searched)
    except ValueError: 
        print("Numbers are the only allowed characters.")
    except:
        print("An unexpected error occurred. Please check your choice against the list and try again.")
    else:
        for recipe in data['recipes_list']:
            if ingredient_searched in recipe['ingredients']:
                print(recipe)

filename = input("Enter the file you are searching through: ")

try: 
    file = open(filename, 'rb')
    data = pickle.load(file)
    print('File loaded')
except FileNotFoundError:
    print('We could not find that file.')
except:
    print('Something went wrong, please try again.')
else: 
    search_ingredient(data)
    file.close()


file = open('recipe_list.bin', 'rb')
data = pickle.load(file)
file.close()