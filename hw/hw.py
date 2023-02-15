def distance(x1, y1, x2, y2):
    z = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return z

x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())

print(distance(x1, y1, x2, y2))