recipes_list = []
ingredients_list = []

def take_recipe():
    a = input("Name of the recipe: ")
    b = int(input("Cook time for the recipe: "))
    c = input("Ingredients in recipe separated by a comma: ").split(", ")
    recipe = {'name': a, 'cooking_time': b, 'ingredients': c}

    return recipe

n = int(input("How many recipes are you adding?: "))

for i in range(n):
    recipe = take_recipe()
    for ingredient in recipe['ingredients']:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
    recipes_list.append(recipe)

for recipe in recipes_list:
    if recipe['cooking_time'] <= 10 and len(recipe['ingredients']) <= 4:
        recipe['difficulty'] = 'easy'
    elif recipe['cooking_time'] <= 10 and len(recipe['ingredients']) > 4:
        recipe['difficulty'] = "moderate"
    elif recipe['cooking_time'] > 10 and len(recipe['ingredients']) <= 4:
        recipe['difficulty'] = "intermediate"
    elif recipe['cooking_time'] > 10 and len(recipe['ingredients']) > 4:
        recipe['difficulty'] = "hard"

for recipe in recipes_list:
    print("Recipe: " + recipe['name'])
    print("Cooking Time: " + str(recipe['cooking_time']) + " minutes")
    print("Difficulty level: " + recipe['difficulty'])
    print("Ingredients: ")
    for position, ingredient in enumerate(recipe['ingredients']):
        print(str(position + 1) + ", " + ingredient)
    ingredients_list.sort()

print("-------------Ingredients Needed for all---------------")
for ingredients in ingredients_list: 
    print(ingredients.capitalize())