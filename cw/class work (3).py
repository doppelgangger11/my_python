n = 5

a = [[0] * n for i in range(n)]

for i in range(len(a)):
    a[i][-1 -i] = 1

for i in range(len(a)): 
    print(a[i])