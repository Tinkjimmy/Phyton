import pickle

def display_recipe(recipe):
    print(recipe)

def search_ingredient(data):
    global number
    for index,ingredient in enumerate(data["all_ingredients"]):
        print("Ingredient N°", index, " : ", ingredient)
      
    try:
        number=int(input("select the number of the ingredient you are searching: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    else:
        for index,ingredient in enumerate(data["all_ingredients"]):
            
            if index == number :
                ingredient_searched= ingredient
            else:
                continue

    for recipe in data['recipes_list']:
        if ingredient_searched in recipe['ingredients']:
            display_recipe(recipe)


file_name=str(input("which file do you want to open? ")) #the user gives the name of the file whrere the object is stored

try:
    with open(file_name,'rb') as file:
        data=pickle.load(file)
        
except FileNotFoundError:
    print('The file', file_name, ' was not found.')

else:
    search_ingredient(data)
    
