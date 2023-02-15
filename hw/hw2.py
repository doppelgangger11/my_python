def pow(x, a):
    if a == 1:
        return x
    elif a == 0:
        return 1
    else:
        return x * pow(x, a - 1)

num = float(input())
stage = int(input())

print(pow(num, stage))