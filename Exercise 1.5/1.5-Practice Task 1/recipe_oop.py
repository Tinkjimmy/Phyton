class Recipe(object):
    difficulty = ""
    all_ingredients = []

    def __init__(self, name, ingredients, cooking_time):
        self.name = name
        self.ingredients = ingredients
        self.cooking_time = cooking_time
        self.update_difficulty()

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time

    def get_cooking_time(self):
        return self.cooking_time

    def add_ingredients(self, new_ingredients):
        # Add new ingredients to the existing list
        self.ingredients.extend(new_ingredients)

        # Call the method to update all ingredients
        self.update_all_ingredients()

    def get_ingredients(self):
        return self.ingredients

    def calculate_difficulty(self):
        if self.cooking_time < 10:
            return "Easy" if len(self.ingredients) < 4 else "Medium"
        else:
            return "Intermediate" if len(self.ingredients) < 4 else "Hard"

    # update the difficulty when ingredients change
    def update_difficulty(self):
        self.difficulty = self.calculate_difficulty()

    # getter for difficulty
    def get_difficulty(self):
        if self.difficulty != "":
            return self.difficulty
        else:
            return self.calculate_difficulty()

    def search_ingredient(self, ingredient):
        return ingredient in self.ingredients

    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if ingredient not in self.all_ingredients:
                self.all_ingredients.append(ingredient)
            else:
                print(ingredient + " is already in the list.")

    def __str__(self):
        output = "\nRecipe: " + str(self.name) + \
                 "\nCooking Time(min): " + str(self.cooking_time) + \
                 "\nDifficulty: " + str(self.difficulty) + \
                 "\nIngredients: " + ', '.join(self.ingredients)
        return output

    # find a recipe with an ingredient
    def recipes_search(data, search_term):
        for recipe in data:
            if recipe.search_ingredient(search_term):
                print(recipe)

# Test your recipes_search method
tea = Recipe("Tea", ["Tea leaves", "Sugar", "Water"], 5)

coffee = Recipe("Coffee", ["Coffee Powder", "Sugar", "Water"], 5)
cake = Recipe("Cake", ["Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking powder", "Milk"], 50)
banana_smoothie = Recipe("Banana Smoothie", ["Bananas", "Milk", "Peanut butter", "Sugar", "Ice Cubes"], 5)

recipes_list = [tea, coffee, cake, banana_smoothie]
Recipe.recipes_search(recipes_list, "Bananas")
