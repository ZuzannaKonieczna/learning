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
        print(i,round(k))
    else:
        k += 5
        k *= -1
        print(i,round(k))
print(round(gora))