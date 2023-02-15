n = int(input())

d = {}

for i in range(n):
    a, b = input().split()
    b = int(b)
    d[a] = b
    
maxi = max(d.values())
mounts = []
for k in d.keys():
    if d[k] == maxi:
        mounts.append(k)
        
mounts = sorted(mounts) 
if len(mounts) == 1:
    print(mounts[0])
else:
    print(mounts[-2]) 