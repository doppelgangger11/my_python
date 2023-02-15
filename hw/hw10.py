#input seconds
n = int(input())
n_h = n // 3600 % 24
n_m = n // 60 % 60
n_s = n % 60

if (n_m < 10):
    n_m = '0' + str(n_m)
else:
    n_m = n_m

if (n_s < 10):
    n_s = '0' + str(n_s)
else:
    n_s = n_s
    
#output hh:mm:ss
print(str(n_h) + ':' + str(n_m) + ':' + str(n_s))