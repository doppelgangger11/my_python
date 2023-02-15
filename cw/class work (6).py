n = int(input())
a = [["."] * n for i in range(n)]
mid = n // 2
for i in range(len(a)):
    a[i][-i - 1] = "*"
    a[i][i] = "*"
    a[mid][i] = "*"
    a[i][mid] = "*"

for d in range(len(a)):
    s = " ".join(a[d])
    print(s)