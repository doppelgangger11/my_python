c = int(input())
m = []

for i in range(c):
    x1 = []
    x2 = []
    a, b = input().split()
    if a[0] == '0':
        x1.append(0)
    if b[0] == '0':
        x2.append(0)
    a, b = int(a), int(b)
    while a // 10 != 0:
        x1.append(a % 10)
        a //= 10
    x1.append(a)
    while b // 10 != 0:
        x2.append(b % 10)
        b //= 10
    x2.append(b)
    x1.sort(reverse=True), x2.sort(reverse=True)
    x1 = set(x1)
    x2 = set(x2)
    if x1 == x2:
        m.append('YES')
    else:
        m.append('NO')

for h in m:
    print(h)