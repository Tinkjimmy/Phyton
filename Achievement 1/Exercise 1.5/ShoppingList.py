# class Date(object):
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year

#     def get_date(self):
#         output = str(self.day) + "/" + str(self.month) + "/" + str(self.year)
#         return output
#     def is_leap_year(self): 
#         return self.year % 4 == 0
#     def is_valid_date(self):
#         if not(type(self.day))== int and type(self.month)== int  :
#             return False
#         if  not type(self.year)==int:
#             return False
#         elif self.year < 0:
#             return False
#         if self.year < 0 :
#             return False
#         if self.month < 1 or self.month >12:
#             return False
#         last_dates = {
#                 1: 31,
#                 2: 29 if self.is_leap_year() else 28,
#                 3: 31,
#                 4: 30,
#                 5: 31,
#                 6: 30,
#                 7: 31,
#                 8: 31,
#                 9: 30,
#                 10: 31,
#                 11: 30,
#                 12: 31
#             }
#         if self.day<1 or self.day>last_dates.get(self.month):
#             return False
#         return True
# date1 = Date(29, 2, 2000)
# date2 = Date(29, 2, 2001) 
# date3 = Date('abc', 'def', 'ghi')

# print(str(date1.get_date()) + ":" + str(date1.is_valid_date()))
# print(str(date3.get_date()) + ": " + str(date3.is_valid_date()))


class ShoppingList(object):
    def __init__(self,list_name,shopping_list = None):
           self.list_name = list_name
           self.shopping_list = shopping_list if shopping_list is not None else []

    def add_item(self, item):
            
            if not item in self.shopping_list:
              self.shopping_list.append(item)
    def remove_item(self, item):
            try:
              self.shopping_list.remove(item)
            except:
              print("Item not found.")
    def view_list(self):
            print("\nItems in " + str(self.list_name) + '\n' + 30*'-')
            for item in self.shopping_list:
              print(' - ' + str(item))
    def merge_lists(self,obj):
        merged_lists_name='Merged List - ' + str(self.list_name) + "+" + str(obj.list_name)
        merged_lists_obj = ShoppingList(merged_lists_name)
        merged_lists_obj.shopping_list= self.shopping_list.copy()

         #adding second list to new object
        for item in obj.shopping_list:
              if not item in merged_lists_obj.shopping_list:
                   merged_lists_obj.shopping_list.append(item)
        return merged_lists_obj
        


pet_store_list = ShoppingList('Pet Store List')
grocery_store_list = ShoppingList('Grocery Store List')

for item in ['dog food', 'frisbee', 'bowl', 'collars', 'flea collars']:
    pet_store_list.add_item(item)

for item in ['fruits' ,'vegetables', 'bowl', 'ice cream']:
    grocery_store_list.add_item(item)

merged_list = ShoppingList.merge_lists(pet_store_list, grocery_store_list)
merged_list.view_list()

        
                
        

        
