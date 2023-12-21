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
    
class Human(Animal):
    def __init__(self,name,age):
        Animal.__init__(self,age)
        self.set_name(name)
        self.friends=[]        
    def add_friend(self,friend_name):
        self.friends.append(friend_name)

    def show_friends(self):
        for friend in self.friends:
            print(friend)
    def speak(self):
        print("hello my name is " + self.name + "!")
    def __str__(self):
        output = "\nClass: Human\nName: " + str(self.name) + \
            "\nAge: " + str(self.age) + "\nFriends list: \n"
        for friend in self.friends:
            output += friend + "\n"
        return output
    
human = Human("Tobias", 35)
human.add_friend("Robert")
human.add_friend("Élise")
human.add_friend("Abdullah")
human.add_friend("Asha")
human.add_friend("Lupita")
human.add_friend("Saito")
human.speak()
print(human)
