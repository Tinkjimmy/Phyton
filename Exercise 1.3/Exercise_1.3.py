recipes_list=[]
ingredients_list=[]
n=int(input("How many recipes do you want to enter? "))

def take_recipe():
    global n
    global ingredients_list
    global recipes_list

    for i in range(n) :
        name=str(input("insert name of the recipe: "))
        cooking_time=int(input("insert cooking time in minutes: "))
        list_=input("Write the ingredients separated by commas")
        ingredients = list_.split(',')
        recipe = {'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients}
        
        
        for ingredient in recipe["ingredients"] :
            if ingredient in ingredients_list:
                print("already in the list")
            else:
                 ingredients_list.append(ingredient)
               
        recipes_list.append(recipe)    

    for recipe in recipes_list:
            if recipe["cooking_time"] <10:
                difficulty="Easy"
            elif  recipe["cooking_time"] <10 and len(recipe["ingredients"])>= 4:
                difficulty="Medium"
            elif  recipe["cooking_time"] >=10 and len(recipe["ingredients"])<= 4:
                difficulty="Intermediate"
            elif  recipe["cooking_time"] >=10 and len(recipe["ingredients"])>= 4:
                difficulty="Hard"
            
            recipe["Difficulty"]=difficulty

            
    
    for recipe in recipes_list:
            print("Recipe: ", recipe['name'])
            print("Cooking Time (min): ", recipe['cooking_time'], " minutes")
            print("Ingredients: ")
            for ingredient in recipe["ingredients"]:
                 print(ingredient)
                    
            print("Difficulty level: ", recipe['Difficulty'])
    
    print("Ingredients Available Acroso All Recipes")
    print("----------------------------------------")
    for ingredient in ingredients_list:
         print(ingredient)

       
take_recipe()







