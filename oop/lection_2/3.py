from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.Pi = 3.14
    
    def area(self):
        print("area >>> ")
        print(self.Pi * (self.radius ** 2))
    
    def perimeter(self):
        print("perimeter >>> ")
        print(self.radius * (2 * self.Pi))

class Rectengle(Shape):
    def __init__(self, a_side, b_side):
        self.a = a_side
        self.b = b_side
    
    def area(self):
        print("area >>> ")
        print(self.a * self.b)

    def perimeter(self):
        print("perimeter >>> ")
        print((self.a + self.b) * 2)


c1 = Circle(12)
c1.area()
c1.perimeter()


r1 = Rectengle(3, 10)
r1.area()
r1.perimeter()