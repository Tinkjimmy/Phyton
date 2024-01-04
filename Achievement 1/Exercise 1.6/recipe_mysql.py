import mysql.connector
conn = mysql.connector.connect(host='localhost',user='cf-python',password='password')
cursor = conn.cursor()

#creating database
cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")
cursor.execute("USE task_database")

cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes(id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50),ingredients VARCHAR(255), cooking_time  INT, difficulty VARCHAR(20))''')

def calculate_difficulty(cooking_time,ingredients):
        if cooking_time < 10:
            return "Easy" if len(ingredients) < 4 else "Medium"
        else:
            return "Intermediate" if len(ingredients) < 4 else "Hard"
        
def create_recipe(conn, cursor):
    name = str(input("name of the recipe: "))
    cooking_time = int(input("time to cook it: "))
    ingredients = input("write ingredients separated by a commas: ")
    difficulty = calculate_difficulty(cooking_time, ingredients.split(','))

    ingredients_list = ", ".join(ingredients.split(','))

    sql_query = "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)"
    val = (name, ingredients_list, cooking_time, difficulty)
    cursor.execute(sql_query, val)
    conn.commit()


def search_recipe(conn, cursor):
    # Step 1: Retrieve the list of ingredients
    cursor.execute("SELECT DISTINCT TRIM(ingredients) FROM Recipes")
    results = cursor.fetchall()

    # Step 2: Extract unique ingredients from the results
    all_ingredients = set()
    for row in results:
        ingredients_list = row[0].split(',')
        all_ingredients.update(map(str.strip, map(str, ingredients_list)))

    all_ingredients = sorted(all_ingredients)

    # Display all ingredients to the user
    for index, ingredient in enumerate(all_ingredients, start=1):
        print(f" Ingredient {index}: {ingredient}")

    # Step 3: User chooses an ingredient to search
    search_ingredient_index = input("Choose the ingredient to search (number): ")

    try:
        search_ingredient_index = int(search_ingredient_index)
        if 1 <= search_ingredient_index <= len(all_ingredients):
            search_ingredient = all_ingredients[search_ingredient_index - 1]
            print(f"Searching for recipes with ingredient: {search_ingredient}")

            # Step 4: Build and execute the SQL query with % wildcard
            query = "SELECT name FROM Recipes WHERE TRIM(ingredients) LIKE %s"
            cursor.execute(query, ('%' + search_ingredient + '%',))
            result = cursor.fetchall()

            # Step 5: Display the results to the user
            if result:
                print("Recipes found:")
                for name in result:
                    print(name[0])
            else:
                print("No recipes found with the specified ingredient.")

        else:
            print("Invalid input. Please enter a valid ingredient number.")
    except ValueError:
        print("Invalid input. Please enter a valid ingredient number.")
















def update_recipe(conn, cursor):
    cursor.execute("SELECT * FROM Recipes")
    result = cursor.fetchall()
    for row in result:
        print("ID: ", row[0])
        print("Name: ", row[1])
        print("Ingredients: ", row[2])
        print("Cooking time(min): ", row[3])
        print("Difficulty: ", row[4])
        print()

    selected_id_input = input("Enter the recipe's ID to update: ")

    try:
        selected_id = int(selected_id_input)
    except ValueError:
        print("Invalid input. Please enter a valid recipe ID.")
        return

    cursor.execute("SELECT * FROM Recipes WHERE id = %s", (selected_id,))
    recipe_to_update = cursor.fetchone()  # Fetch the recipe as a tuple

    response_name = input("Do you want to update the name(y/n): ")
    if response_name.lower() == 'y':
        new_name = input("Enter the new name: ")
    else:
        new_name = recipe_to_update[1]

    response_ingredients = input("Do you want to update the ingredients (y/n): ")
    if response_ingredients.lower() == 'y':
        new_ingredients = input("Enter the new ingredients separated by commas: ")
    else:
        new_ingredients = recipe_to_update[2]

    response_cooking_time = input("Do you want to update the cooking time (y/n): ")
    if response_cooking_time.lower() == 'y':
        new_cooking_time = int(input("Enter the new cooking time: "))
    else:
        new_cooking_time = recipe_to_update[3]

    updated_difficulty = calculate_difficulty(new_cooking_time, new_ingredients)

    cursor.execute(
        "UPDATE Recipes SET name = %s, ingredients = %s, cooking_time = %s, difficulty = %s WHERE id = %s",
        (new_name, new_ingredients, new_cooking_time, updated_difficulty, selected_id)
    )
    conn.commit()

    print("Recipe updated successfully!")



    
def delete_recipe(conn, cursor):
    cursor.execute("SELECT * FROM Recipes")
    result = cursor.fetchall()  # Call fetchall to retrieve the results

    for row in result:
        print("ID: ", row[0])
        print("Name: ", row[1])
        print("Ingredients: ", row[2])
        print("Cooking time(min): ", row[3])
        print("Difficulty: ", row[4])
        print()

    recipe_name_to_delete = input("Enter the name of the recipe to delete: ")

    cursor.execute("DELETE FROM Recipes WHERE name = %s", (recipe_name_to_delete,))
    conn.commit()

    print(f"Recipe '{recipe_name_to_delete}' deleted successfully!")
    

def main_menu(conn,cursor):
    choice = ""
    while (choice != 'quit!'):
        print("What would you like to do? Pick a choice!")
        print("1. Perform create_recipe")
        print("2. Perform search_recipe ")
        print("3. Perform update_recipe")
        print("4. Perform delete_recipe")

        print("Type 'quit' to exit the program.")
        choice= input("Your choice : ")

        if choice == '1':
            create_recipe(conn,cursor)
        elif choice == '2':
            search_recipe(conn,cursor)
        elif choice == '3':
            update_recipe(conn,cursor)
        elif choice == '4':
            delete_recipe(conn,cursor)

main_menu(conn,cursor)

cursor.close()
conn.close()
