import pickle
import os

print("Current Working Directory:", os.getcwd())

def calc_difficulty(recipe):
    if recipe["cooking_time"] <10:
        difficulty="Easy"
    elif  recipe["cooking_time"] <10 and len(recipe["ingredients"])>= 4:
        difficulty="Medium"
    elif  recipe["cooking_time"] >=10 and len(recipe["ingredients"])<= 4:
        difficulty="Intermediate"
    elif  recipe["cooking_time"] >=10 and len(recipe["ingredients"])>= 4:
        difficulty="Hard"
    recipe["Difficulty"]=difficulty


def take_recipe():
    global recipes_list
    global all_ingredients
#user inserts recipe    
    name=str(input("insert name of the recipe: "))
    cooking_time=int(input("insert cooking time in minutes: "))
    list_=input("Write the ingredients separated by commas ")
    ingredients = list_.split(',')
    recipe = {'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients}

# checking if the ingredients aare already in the all_ingredients list
    for ingredient in recipe["ingredients"] :
        if ingredient in all_ingredients:
            print("already in the list")
        else:
            all_ingredients.append(ingredient)
# calculating difficulty level
    calc_difficulty(recipe)  
    return recipe

# data = {'recipes_list': [], 'all_ingredients': []}

try:
    file_name=str(input("which file do you want to open? ")) #the user gives the name of the file whrere the object is stored
    with open(file_name,'rb') as file:
        data=pickle.load(file)
except FileNotFoundError:
    print('The file', file_name, ' was not found.')
    data = {'recipes_list':[],'all_ingredients':[]}
except Exception as e:
    data = {'recipes_list':[],'all_ingredients':[]}
else:
    with open(file_name,'rb') as file:
        data=pickle.load(file)   #this line stores the object in data
finally:
    recipes_list=data['recipes_list']
    all_ingredients=data['all_ingredients']


n=int(input("How many recipes do you want to enter? "))

for i in range(n):
     recipe=take_recipe()
     recipes_list.append(recipe)

#reuniting recipes_list and all-ingredients list

recipes_data = {
    'recipes_list': recipes_list,
    'all_ingredients': all_ingredients
}
with open(file_name,'wb') as file:
    pickle.dump(recipes_data,file)