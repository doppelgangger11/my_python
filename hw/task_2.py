# input data

ck = int(input())
keys = [int(i) for i in input().split()]

cp = int(input())
keypushs = [int(i) for i in input().split()]

# calulating the resault after work on the eybord

for i in keypushs:
    keys[i - 1] -= 1
    # print(keys)

# analyze and creating the output

for i in range(ck):
    if keys[i] < 0:
        print('yes')
    else:
        print('no')