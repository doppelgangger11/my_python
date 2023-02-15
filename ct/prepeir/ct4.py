n = input()
c = ['a', 'b', 'c']
cc = str()
for i in range(len(n)):
    if n[i] != 'a' and n[i] != 'b' and n[i] != 'c':
        cc += n[i]
print(cc)