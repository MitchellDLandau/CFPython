import pickle

recipes_list = []
ingredients_list = []

def calc_difficulty(b, c):    
        if b <= 10 and len(c) <= 4:
            return 'easy'
        elif b <= 10 and len(c) > 4:
            return "moderate"
        elif b > 10 and len(c) <= 4:
            return "intermediate"
        elif b > 10 and len(c) > 4:
            return "hard"

def take_recipe():
    a = input("Name of the recipe: ")
    b = int(input("Cook time for the recipe: "))
    c = input("Ingredients in recipe separated by a comma: ").split(", ")
    d = calc_difficulty(b, c)
    recipe = {'name': a, 'cooking_time': b, 'ingredients': c, 'difficulty': d}
    return recipe

n = int(input("How many recipes are you adding?: "))

for i in range(n):
    recipe = take_recipe()
    for ingredient in recipe['ingredients']:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
    recipes_list.append(recipe)
    print(recipe['name'] + ' has been added.')
        
filename = input("Enter the file you are saving to: ")
try: 
     with open(filename, 'rb') as file:
        data = pickle.load(file)
     print('File loaded.')
     recipes_list.extend(data['recipes_list'])
     ingredients_list.extend(data['ingredients_list'])
except FileNotFoundError:
     print('We could not find that file.')
except Exception as e:
     print('Something went wrong: ', e)

data = {'recipes_list': recipes_list, 'ingredients_list': ingredients_list}

with open(filename, 'wb') as my_file:
    pickle.dump(data, my_file)
    print('Recipe data has been saved.')