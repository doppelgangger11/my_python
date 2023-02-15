class Animals:
    def __init__(self, food, location):
        self.food = food
        self.loc = location
    def make_noise(self):
        print("Animal is noising")
    def eat(self):
        print("Animal is eating")
    def sleep(self):
        print("Animal is sleeping")

class Dog(Animals):
    def __init__(self, name, food, location):
        super().__init__(food, location)
        self.name = name
    def make_noise(self):
        print(self.name, "says >>> 'Woof!'")
    def eat(self):
        print("shhh", self.name, "is sleeping")
    def sleep(self):
        print("shhh", self.name, "is sleeping")

class Cat(Animals):
    def __init__(self, name, food, location):
        super().__init__(food, location)
        self.name = name
    def make_noise(self):
        print(self.name, "says >>> 'Meeaaauu!'")
    def eat(self):
        print("shhh", self.name, "is sleeping")
    def sleep(self):
        print("shhh", self.name, "is sleeping")
            
class Horse(Animals):
    def __init__(self, name, food, location):
        super().__init__(food, location)
        self.name = name
    def make_noise(self):
        print(self.name, "says >>> 'Frr!'")
    def eat(self):
        print("shhh", self.name, "is sleeping")
    def sleep(self):
        print("shhh", self.name, "is sleeping")

class Vet:
    def treat_animal(self, animal):
        print("--------------------")
        print(animal.name, animal.food, animal.loc)
        animal.sleep()

d1 = Dog("Archi", "beef", "home")
d2 = Dog("Rex", "beef", "home")
d3 = Dog("Dog", "beef", "home")
c1 = Cat("Marsik", "fish", "home")
c2 = Cat("Mursik", "whiskas", "home")
h1 = Horse("Hunter", "weet", "field")
v = Vet()
l = [d1, d2, d3, c1, c2, h1]

for i in l:
    v.treat_animal(i)