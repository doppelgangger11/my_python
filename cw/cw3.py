class Point:
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def dist(self):
        print(((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)**0.5)

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
print(((x2 - x1)**2 + (y2 - y1)**2)**0.5)
inp = Point(x1, x2, y1, y2)
inp.dist()