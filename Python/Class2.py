class Animal:
    def __init__(self, name):  # Corrected constructor
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing.")

# Creating instances
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Calling methods
dog.eat()
dog.bark()
cat.eat()
cat.meow()


class Animal:
    def make__sound(self):
        print("Some generic animal sound")
class dog(Animal):
    def make_sound(seelf):
        print("Woof")
class cat(Animal):
    def make_sound(self):
        print("Meow")
class bird(Animal):
    def make_sound(self):
        print("Tweel")
#polymorphic behavior
animals=[dog(),cat(),bird()]
for animal in animals:
    animal.make_sound()
