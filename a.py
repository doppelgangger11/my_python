# x1, y1 = int(input()), int(input())
# x2, y2 = int(input()), int(input())

# if x1 + 1 == x2 or x2 + 1 == x1:
#     print('YES')
# elif y1 + 1 == y2 or y2 + 1 == y1:
#     print('YES')
# else:
#     print('NO')

a = [int(j) for j in input().split() for i in range(3)]


for i in range(len(a)):
    s = 0
    for j in range(len(a[i])):
        s = s + a[i][j]
    print(s, end=" ")