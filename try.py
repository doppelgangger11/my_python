text = []
for i in range(int(input())):
    text.append(input().split())


dick = {}
for i in range(len(text)):
    for j in range(len(text[i])):
        if text[i][j] not in dick:
            dick[text[i][j]] = text[i].count(text[i][j])
        else:
            dick[text[i][j]] += text[i].count(text[i][j])
answer = []
for i in dick.keys():
    answer.append((i, dick[i]))
    answer.sort(key = lambda x: x[1], reverse= True)
    print(i)

for i in range(len(answer)):
    answer.sort(key= lambda x: x[1], reverse=True)
print(answer)