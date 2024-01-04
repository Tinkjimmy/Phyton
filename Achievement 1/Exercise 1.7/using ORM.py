#insert new item in a table (Stock) with an ORm:

new_item = Stock(
        item_id = 1,
        item_name = "Water",
        manufacturer_name = "Aquafina",
        price = 10,
        quantity = 20
)

session.add(new_item)
session.commit()

#declaring a class that contains the table
class Recipe(Base):
         __tablename__= "recipes"
         id= Column(Integer,primary_key=True, autoincrement=True)
         name= Column(String(50))
         ingredients= Column(String(255))
         cooking_time = Column(Integer)
         difficulty = Column(String(20))
         def __repr__(self):
             return"<Recipe ID: " + str(self.id) + "-" + self.name + ">"
         
#creating the table
Base.metadata.create_all(engine)



#using session to add instances to a table:
Cake = Recipe (
    ...: name = "Cake",
    ...: cooking_time =  50,
    ...: ingredients = "Sugar,Butter,Eggs,Vanilla essence,Flour,Backing Powder,Milk")
session.add(tea)
session.commit()


#pulling enteries from a table as objects

#accedo a tutte le istanze della tabella
session.query(Recipe).all()

#inserisco tutte le istaze in una variabile
recipes_list=session.query(Recipe).all()

#accedo alle variabili e alle loro proprietà
recipes_list[0].id

#printing the objects in the list:

for recipe in recipes_list:
    print("Recipe ID: ", recipe.id)
    print("Recipe Name: ", recipe.name)
    print("Ingredients: ", recipe.ingredients)
    print("Cooking Time: ", recipe.cooking_time)

#Retrieving a Single Object Using the get() Method
    
    session.query(Recipe).get(1)
#Retrieving One or More Objects Using the filter() Method
    session.query(<model name>).filter(<model name>.<attribute/column name> == <value to compare against>) #this will return a query object and it need another query(chained) to return the object out
    
    #i need to chain other methos to the query:

all(): # returns a list of all objects from the query (output type: list)
one(): #returns only one object, if only one object is resultant from your query (output type: object from your table)
first(): # returns the first object from a list of results (output type: object from your table)
get(id): # returns an object with an id that matches with the primary key (output type: object from your table)

#Using the like() Method

session.query(Recipe).filter(Recipe.ingredients.like("%Water%")).all()

#concatenate like()

session.query(Recipe).filter(Recipe.ingredients.like("%Milk%"), Recipe.ingredients.like("%Baking Powder%")).all()

#i can also use this way:
condition_list = [
Recipe.ingredients.like("%Milk%"),
Recipe.ingredients.like("%Baking Powder%")
]
# Use the * before condition_list to unpack items out of the list
session.query(Recipe).filter(*condition_list).all()

#Updating Entries in Your Table
recipes_list[0].ingredients += ', Cardamom'

session.commit() #commit the changes to the database


#Making Direct Changes(in the database) Using the update() Method

    session.query(Recipe).filter(Recipe.name == 'Cake').update({Recipe.name: 'Birthday Cake'}) #renaming recipe's name
    session.commit()

#Deleting Entries from Your Table
#retrieve the the entry as an object
recipe_to_be_deleted = session.query(Recipe).filter(Recipe.name == 'Buttered Toast').one()
#use the delete() method of session
session.delete(recipe_to_be_deleted)
session.commit()