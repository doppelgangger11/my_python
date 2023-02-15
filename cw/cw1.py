class Point:
    def __init__(self, x, y):
        self.x_y = {"x" : x, "y" : y}
    def get_out(self, a):
        print(self.x_y[a])

c = input()
inp = Point(5, 10)
inp.get_out(c)