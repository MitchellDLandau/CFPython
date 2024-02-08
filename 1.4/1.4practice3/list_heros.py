def display(file):
    heroes = []
    for line in file:
        line = line.strip('\n')
        hero_name = line.split(", ")[0]
        first_apperance = line.split(', ')[1]
        heroes.append([hero_name, first_apperance])
    heroes.sort(key = lambda hero: hero[1])
    for hero in heroes:
        print("--------------------------")
        print("Superhero: " + hero[0])
        print("First apperance year: " + hero[1])

filename = input("super_heros.txt")
try: 
    file = open("super_heros.txt", 'r')
    display(file)
except FileNotFoundError:
    print('file does not exist')
except:
    print('an unexpected error happened')
else: 
    file.close()
finally: 
    print('goodbye')