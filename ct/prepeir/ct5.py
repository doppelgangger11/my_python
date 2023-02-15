n = int(input())
d = {}
for i in range(n):
    a, b = input().split()
    b = int(b)
    if a and b not in d:
        d[a] = d.get(a, 0) + b
min = 9999
for j in d.values():
    if j < min:
        min = j

c = []
for key, values in sorted(d.items()):
    if values == min:
        c.append(key)
c.sort()

print(c[0])