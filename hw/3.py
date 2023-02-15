my_list = [ 1, 2, 3, 4 ]

print(my_list)

print("-----------------")

str(my_list)

a = my_list.split(", ")

print(a)

print("-----------------")

list(my_list)

for i in range(len(my_list)):
    my_list[i] = int(my_list[i])
print(my_list)

print("-----------------")

a = ["a", 'b', 'c', 'd']

s = "|||".join(a)

print(s)