class Matrix:
    def __init__(self, matrix_a):
        self.a = matrix_a

    def summ(self, b):
        c = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
        for i in range(len(self.a)):
            for j in range(len(self.a[i])):
                c[i][j] += self.a[i][j] + b[i][j]
        for i in range(len(c)):
            print(c[i])

print("Please enter the first Matrix: ")

a = [[int(i) for i in input().split()] for j in range(3)]

print("Please enter the second Matrix: ")

b = [[int(i) for i in input().split()] for j in range(3)]

d = Matrix(a)

d.summ(b)