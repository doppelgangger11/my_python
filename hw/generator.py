my_list = [i**2 for i in range(5)]

print (my_list)

print("--------------")

s = "8 9 -2 342 1"
a = s.split()

print(a)

print("--------------")

b = [int(x) for x in a]

print(b)

print("--------------")

c = [0 for i in input().split()]
print(c)