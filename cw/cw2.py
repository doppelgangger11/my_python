class Point:
    def __init__(self, x, y):
        self.x_y = {'x' : x, 'y' : y}
    def get_out(self, a):
        print(self.x_y[a])

x = input()
y = input()
c = input()

inp = Point(x, y)

inp.get_out(c)