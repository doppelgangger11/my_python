n = 5

# a = []
# for i in range(len(n)):
#     b = [0] * n
#     a.append(b)

a = [[0] * n for i in range(n)]

# a[2][3] = 1

for i in range(len(a)):
    a[i][i] = 1

for i in range(len(a)): 
    print(a[i])
