n = int(input())
a = [[int(x) for x in input().split()] for i in range(n)]
c = 0
c1 = 0
for i in range(len(a)):
    c += a[0][i - 1]
    c += a[i - 1][-1]
    c += a[-1][i - 1]
    c += a[i - 1][0]
    c1 = c - (a[0][0] + a[0][-1] + a[-1][0] + a[-1][-1])

print(c1)
