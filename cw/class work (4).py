A = []
n = 3
# for i in range(n):
#     a = [int(i) for i in input().split()]
#     A.append(a)

# n = [int(i) for i in input().split()]

A = [[int(i) for i in input().split()] for i in range(n)]

for c in range(len(A)):
    print(A[c])