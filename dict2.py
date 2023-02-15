countr = {}

for i in range(int(input())):
    coun, *city = input().split()
    countr[coun] = city

touns = []
for i in range(int(input())):
    touns.append(input())

# print(countr, touns)
answer = []
for i in countr.keys():
    for j in range(len(touns)):
        if touns[j] in countr[i]:
            answer.append(i)
answer.reverse()

for i in range(len(answer)):
    print(answer[i])