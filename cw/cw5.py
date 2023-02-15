import math
class Rect:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def get_perimeter(self):
        print(2 * (self.x + self.y))
    def get_area(self):
        print (self.x * self.y)
    def get_diagonal(self):
        print(round(((self.x**2 + self.y**2)**0.5), 2))
x, y = int(input()), int(input())

inp = Rect(x, y)
inp.get_perimeter()
inp.get_area()
inp.get_diagonal()