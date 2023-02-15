n = int(input())

a = [[0] * n for i in range(n)]


for i in range(len(a)):
    for j in range(len(a[i])):
        if j < i:
            a[i][j] = 1

for i in range(len(a)): 
    print(a.joint)