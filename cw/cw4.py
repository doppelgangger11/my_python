class Rect:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def is_square(self):
        a = self.x == self.y
        print(a)
x, y = int(input()), int(input())

inp = Rect(x, y)
inp.is_square()
