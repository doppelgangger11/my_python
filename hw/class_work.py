# dic[x] = dic.get(x, 0) + 1


# if a < dic.values(x):
#             a = dic.values(x)
c = int(input())
dic = {}

for i in range(c):
    l = input().split()
    for x in l:
        dic[x] = dic.get(x, 0) + 1
           
maxv = max(dic.values())
max_elements = []

for i in dic:
    if dic[i] == maxv:
        max_elements.append(i)      

print(min(max_elements))