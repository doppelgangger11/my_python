class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, year, fac):
        super().__init__(name, age) # or Person.__init__(name, age)
        self.year = year
        self.fac = fac

s1 = Student("Mike", 21, 3, "IT")
print(s1.name)