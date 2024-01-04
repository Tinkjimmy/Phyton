from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import or_



Base = declarative_base()
engine = create_engine("mysql://cf-python:password@localhost/task_database")
Session = sessionmaker(bind=engine)
session = Session()
#defining the Recipe model
class Recipe(Base):
        __tablename__= "final_recipes"
        id= Column(Integer,primary_key=True, autoincrement=True)
        name= Column(String(50))
        ingredients= Column(String(255))
        cooking_time = Column(Integer)
        difficulty = Column(String(20))
        def __repr__(self):
            return"<Recipe ID: " + str(self.id) + "-" + self.name + "-" + self.difficulty + ">"
        def __str__(self):
            ingredients_list = self.ingredients.split(", ")
            ingredients_column = "\n".join(f"\t- {ingredient}" for ingredient in ingredients_list)
            print("-" * 30)

            return (
                f"Name of the recipe: {self.name}\n"
                + f"\tId: {self.id}\n"
                + f"Difficulty: {self.difficulty}\n"
                + "Ingredients:\n" + ingredients_column + "\n"
                + "-" * 30
            )
        
        def calculate_difficulty(self):
            if self.cooking_time < 10:
                self.difficulty = "Easy" if len(self.ingredients) < 4 else "Medium"
            else:
                self.difficulty = "Intermediate" if len(self.ingredients) < 4 else "Hard"
        def return_ingredients_as_list(self):
            if self.ingredients == []:
                ingredients=[]
            else:
                ingredients = self.ingredients.split(",")
             
Base.metadata.create_all(engine)

def create_recipe():
    name = input("Name of the recipe: ")

    if len(name) > 50 or not isinstance(name, str):
        print("The name of this recipe is too long or contains invalid characters.")
        return

    cooking_time_input = input("Time to cook it: ")

    # Check if cooking_time is numeric
    if not cooking_time_input.isdigit():
        print("Cooking time must be a number.")
        return

    cooking_time = int(cooking_time_input)

    ingredients = []
    try:
        num_ingredients = int(input("How many ingredients in this recipe?"))
    except ValueError:
        print("Invalid input. Please enter a number for the ingredients.")
        return

    # Letting the user create the ingredients list
    for i in range(1, num_ingredients + 1):
        ingredient = input(f"Insert ingredient N°{i}: ")
        if not isinstance(ingredient, str):
            print("This ingredient has numbers in it.")
            return
        else:
            ingredients.append(ingredient)

    if len(ingredients) > 255:
        print("The list of ingredients is too long.")
        return
    else:
        ingredients = ', '.join(ingredients)

    # Creating a new object from the Recipe class
    recipe_entry = Recipe(
        name=name,
        cooking_time=cooking_time,
        ingredients=ingredients,
    )
    recipe_entry.calculate_difficulty()

    # Committing the object to the database
    session.add(recipe_entry)
    session.commit()

# printing all the recipes in the daabase in a well formatted manner
def view_all_recipes():
    recipes_list = session.query(Recipe).all()

    if not recipes_list:
        print("No recipes found.")
    else:
        for recipe in recipes_list:
            print(recipe)


def search_by_ingredient():
    all_ingredients = set()
    if session.query(Recipe).count() == 0:
        print("This table doesn't have any recipes.")
        return
    else:
        results = session.query(Recipe.ingredients).all()
        temp_list = []
        for result in results:
            temp_list = result[0].split(",")
            temp_list = {ingredient.strip() for ingredient in temp_list}  # Strip whitespaces and use a set
            all_ingredients.update(temp_list)
        all_ingredients = sorted(all_ingredients)

        for index, ingredient in enumerate(all_ingredients, start=1):
            print(f" Ingredient {index}: {ingredient}")

        user_choice = input("Choose the ingredients you would like to search (write the numbers separated by spaces): ")
        user_choices = user_choice.split(" ")
        temp_search_list = []

        for choice in user_choices:
            if not choice.isdigit():
                print(f"Invalid input: {choice} is not a valid number.")
                return

            choice = int(choice)
            if 1 <= choice <= len(all_ingredients):
                temp_search_list.append(all_ingredients[choice - 1])

        search_ingredients = temp_search_list

    conditions = or_(*(Recipe.ingredients.like(f"%{ingredient}%") for ingredient in search_ingredients))
    recipes_list = session.query(Recipe).filter(conditions).all()

    for recipe in recipes_list:
        print(recipe)

def edit_recipe():
    if session.query(Recipe).count() == 0:
        print("This table doesn't have any recipes")
        return
    else:
        results = session.query(Recipe.id, Recipe.name).all()
        for result in results:
            print(" Recipes id: " + str(result.id) + "\n" + " Recipes name: " + result.name)

        user_choice = input("Choose a recipe to edit (by the id number): ")
        valid_ids = [str(result.id) for result in results]
        if user_choice not in valid_ids:
            print("Invalid recipe ID. Please choose a valid ID.")
            return
        else:
            recipe_to_edit = session.query(Recipe).filter(Recipe.id == user_choice).one()
            print("1. Name: " + recipe_to_edit.name)
            print("2. Ingredients: " + recipe_to_edit.ingredients)
            print("3. Cooking Time: " + str(recipe_to_edit.cooking_time))
            edit_number = int(input("Choose which property to edit (write the number): "))

            if edit_number == 1:
                new_name = input("What is the new name of the recipe? ")
                session.query(Recipe).filter(Recipe.id == user_choice).update({Recipe.name: new_name})
                session.commit()
            elif edit_number == 2:
                new_ingredient = input("What is the new ingredient of the recipe? ")
                recipe_to_edit.ingredients += ", " + new_ingredient
                new_difficulty = recipe_to_edit.calculate_difficulty()
                session.query(Recipe).filter(Recipe.id == user_choice).update({
                    Recipe.ingredients: recipe_to_edit.ingredients,
                    Recipe.difficulty: new_difficulty
                })

                session.commit()
            elif edit_number == 3:
                new_cookingtime = int(input("What is the new cooking time? "))
                recipe_to_edit.cooking_time = new_cookingtime
                new_difficulty = recipe_to_edit.calculate_difficulty()
                session.query(Recipe).filter(Recipe.id == user_choice).update({
                    Recipe.cooking_time: new_cookingtime,
                    Recipe.difficulty: new_difficulty
                })
                session.commit()
            else:
                print("The number you input is not allowed")
                return

#deleting a selected recipe
def delete_recipe():
    if session.query(Recipe).count() == 0 :
        print("this table doesn't have any recipes")
        return
    else:
        results= session.query(Recipe.id, Recipe.name).all()
        for result in results:
            print(" Recipes id: " + str(result.id) + "\n" + " Recipes name: " + result.name )

    user_choice= input("Choose a recipe to delete (by the id number): ")    
    valid_ids = [str(result.id) for result in results]
    if user_choice not in valid_ids:
        print("Invalid recipe ID. Please choose a valid ID.")
        return
    else:
        recipe_to_delete = session.query(Recipe).filter(Recipe.id == user_choice).one()
        user_decision= str(input("Are yousure you wnat to delete the recipe: " + recipe_to_delete.name + " ?"))
        if user_decision.lower() == "yes":
            session.delete(recipe_to_delete)
            session.commit()
        else: 
            return
        

def main_menu():
    choice = ""
    while (choice.lower() != 'quit!'):
        print("What would you like to do? Pick an option!")
        print("1. Perform create_recipe")
        print("2. Perform view_all_recipes ")
        print("3. Perform search_by_ingredient")
        print("4. Perform edit_recipe")
        print("5. Perform delete_recipe")

        print("Type 'quit' to exit the program.")
        choice= input("Your choice(number) : ")

        if choice == '1':
            create_recipe()
        elif choice == '2':
            view_all_recipes()
        elif choice == '3':
            search_by_ingredient()
        elif choice == '4':
            edit_recipe()  
        elif choice == '5':
            delete_recipe()       
        else:
            print("input not valid")
            return

main_menu()


    

                