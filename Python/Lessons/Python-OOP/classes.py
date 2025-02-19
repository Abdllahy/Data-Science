class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner
        
    def bark(self):
        print("whoof! whoof!")

class Owner:
    def __init__(self, name, address, contact):
        self.name = name
        self.address = address
        self.contact = contact

owner1 = Owner("John", "123 Main St", "123-456-7890")    
owner2 = Owner("Jane", "456 Elm St", "987-654-3210")

dog1 = Dog("Bruce", "Bulldog", owner1)
# print(dog1.name)
# print(dog1.breed)
# dog1.bark()
print(dog1.owner.name)


print("------------------")

dog2 = Dog("Buddy", "Golden Retriever", owner2)
# print(dog2.name)
# print(dog2.breed)
# dog2.bark()
print(dog2.owner.name)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and i am {self.age} years old.")

person1 = Person("John", 30)
person1.greet()

person2 = Person("Jane", 25)
person2.greet()