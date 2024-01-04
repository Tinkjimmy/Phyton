# class Person:
#     def walk():
#         print("Hello, i can walk!")

# class Athlete(Person):
#     def run():
#         print("Hey, i can tun too")
        
class Animal(object):
    def __init__(self,age):
        self.age=age
        self.name= None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self,age):
        self.age= age
    def set_name(self,name):
        self.name=name

    def __str__(self):
        output = "\nClass: Animal\nName: " + str(self.name) + \
            "\nAge: " + str(self.age)
        return output
class Cat(Animal):
    def speak(self):
        print("mew")
    def __str__(self):
        output = "\nClass: Cat\nName: " + str(self.name) + \
            "\nAge: " + str(self.age)
        return output
    
class Dog(Animal):
    def speak(self):
        print("Woof!")
    def __str__(self):
        output = "\nClass: Dog\nName: " + str(self.name) + \
            "\nAge: " + str(self.age)
        return output
    
cat= Cat(3)
dog=Dog(5)

cat.set_name("pip")
dog.set_name("bobi")
print(cat)
print(dog)
cat.speak()
dog.speak()