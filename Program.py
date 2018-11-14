# Cookbook (Case Study) by Raquel Dombroskie & Milica Djuric Case Due Dec.1

# Purpose of program: Compare ingredients
# and match with available recipes that can be made.

# Takes ingredients input file.

ingredients = []
recipes = {}

def main():
    ingredients_file = open('ingredients.txt', 'r')
    for line in ingredients_file:
        line = line.rstrip('\n')
        ingredients.append(line)

    selection = 0
    while selection != '6':
        selection = options()
        if selection == '1':
            print("This is what you have:", ingredients)
        elif selection == '2':
            #append to the list and at bottom of program save to ingredients.txt
            ingredient = input("Add ingredient: ")
            ingredients.append(ingredient)
        elif selection == '3':
            to_delete = input("Ingredient to delete: ")
            ingredients.remove(to_delete)
        elif selection == '4':
            recipe_name = input("Recipe name: ")
            recipe_ingredients = input("Enter each ingredient separated by a space: ")
            recipe_list = []
            recipe_list = recipe_ingredients.split()
            recipes[recipe_name] = recipe_list
        elif selection == '5':
            print(recipes)
            
            
    
    ingredients_file = open('ingredients.txt', 'w')
    for item in ingredients:
        ingredients_file.write(item + '\n')
    
    #save dictionary to file with pickel and load it back in






    
def options():
    print("\nOptions")
    print("1) Show ingredients")
    print("2) Add ingredients")
    print("3) Delete ingredients")
    print("4) Add a recipe")
    print("5) See recipes")
    print("6) Quit")
    selection = input("Your choice: ")
    return selection



main()
