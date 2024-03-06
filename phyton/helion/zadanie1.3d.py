m = 5
n = 4
k = 0

if m+n < k:
    print(k)
else:
    k = m +n
    if m+1 < n:
        n *=4
        k = 1
    else: m*=2

print (m,k,n)