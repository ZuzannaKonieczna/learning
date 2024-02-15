n = int(input())
gora = 0
k = -2 #6
dol = 0
l = 3 #4

for i in range(1,n):
    gora+=k
    if (k < 0):
        k *=-1
        k += 5
    else:
        k += 5
        k *= -1
print(round(gora))
for i in range(1,n+1):
    dol+= l
    if (k < 0):
        k*= -1 
        k += 4
    else:
        k += 4
        k*= -1
print (round(dol))
print(round(gora/dol, 2))
