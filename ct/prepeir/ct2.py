n = input().split()
cc = 0
for i in range(len(n)):
    c = n[i]
    if c[0] == 't' and c[-1] == 't':
        cc += 1

print(cc)