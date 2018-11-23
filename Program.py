# Cookbook (Case Study) by Raquel Dombroskie & Milica Djuric Case Due Dec.1

# Purpose of program: Compare ingredients
# and match with available recipes that can be made.

# Takes ingredients input file.
import pickle
ingredients = []
recipes = {}
availablerecipeslist = []

def main():
    ingredients_file = open('ingredients.txt', 'r')
    for line in ingredients_file:
        line = line.rstrip('\n')
        ingredients.append(line)
    

    selection = 0
    while selection != '7':
        selection = options()
        if selection == '1':
            print("\nThis is what you have:", ingredients)
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
        elif selection =='6':
            to_delete = input("Recipe to delete: ")
            del recipes[to_delete]
        elif selection == 'A':
            for key, value in recipes.items():
                numbaofitems = len(value)
                set2 = set(ingredients)
                set1 = set(value)
                set3 = set1.intersection(set2)
                numbaofitems2 = len(set3)
                if numbaofitems2 == numbaofitems:
                    print("\n"+key, set3)
                    availablerecipeslist.append(key)
            
    
    ingredients_file = open('ingredients.txt', 'w')
    for item in ingredients:
        ingredients_file.write(item + '\n')
    ingredients_file.close()

    availablerecipesfile = open('availablerecipes.txt', 'w')
    for item in availablerecipeslist:
        availablerecipesfile.write(item + '\n')
    availablerecipesfile.close()

       
def options():
    print("\n       Cookbook")
    print("       --------\n")
    print("""\
       .--,--.
       `.  ,.'
        |___|
        :o o:   O   
       _`~^~'_  |    
     /'   ^   `\=)
   .'  _______ '~|
   `(<=|     |= /'
       |     |
       |_____|
~~~~~~~ ===== ~~~~~~~~

                    """)
    print("A) See available recipes")
    print("\nOptions")
    print("1) Show ingredients")
    print("2) Add an ingredient")
    print("3) Delete an ingredient")
    print("4) Add a recipe")
    print("5) See recipes")
    print("6) Delete a recipe")
    print("7) Quit")
    selection = input("Your choice: ")
    return selection


#Pickling

input_recipes_file = open('recipes.dat', 'rb')
recipes = pickle.load(input_recipes_file)

main()

recipes_file = open('recipes.dat', 'wb')
pickle.dump(recipes, recipes_file)
recipes_file.close()

