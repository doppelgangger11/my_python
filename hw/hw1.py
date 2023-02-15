def capitalize(x):
    z = []
    for i in range(len(x)):
        z.append(ord(x[i][0]))
        x[i].replace(x[i][0], chr(z[i] - 32))
        print(x[i])
    return x
x = [str(i) for i in input().split()]
print(capitalize(x))