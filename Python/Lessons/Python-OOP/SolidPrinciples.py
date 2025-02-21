# The Liskov Substitution Principle (LSP) states that objects of a superclass should be replaceable with objects of its subclasses without affecting the correctness of the program.
# In other words, a subclass should be able to replace its superclass without any unexpected behavior.

print("Example of Liskov Substitution Principle being met")

class Food:
    def cook(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Pasta(Food):
    def cook(self):
        return "Cooking pasta in boiling water."

class Steak(Food):
    def cook(self):
        return "Grilling steak on a hot grill."

def prepare_food(food: Food):
    print(food.cook())

# Using the classes
pasta = Pasta()
steak = Steak()

prepare_food(pasta)  # Works: "Cooking pasta in boiling water."
prepare_food(steak)  # Works: "Grilling steak on a hot grill."

print("Example of Liskov Substitution Principle not being met")


class Food:
    def cook(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Fruit(Food):
    def cook(self):
        raise Exception("Fruits don't require cooking!")

class Pasta(Food):
    def cook(self):
        return "Cooking pasta in boiling water."

def prepare_food(food: Food):
    print(food.cook())

# Using the classes
pasta = Pasta()
fruit = Fruit()

prepare_food(pasta)  # Works: "Cooking pasta in boiling water."
# prepare_food(fruit)  # Would raise an exception: "Fruits don't require cooking!"


# The hash method in OOP 

class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __eq__(self, other):
        return self.age == other.age and self.name == other.name

    def __hash__(self):
        print('The hash is:')
        return hash((self.age, self.name))

person = Person(23, 'Adam')
print(hash(person))

