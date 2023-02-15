n = [int(x) for x in input().split()]
c = []
for i in range(len(n)):
    if n[i] % 2 != 0 or (n[i] % 2 == 0 and i % 2 == 0):
        c.append(n[i])
for d in range(len(c)):
    print(c[d], end=' ')