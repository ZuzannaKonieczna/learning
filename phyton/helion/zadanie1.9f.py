n = int(input())
gora = 0
dol1 =0
k = -0.2
for i in range (1,n+1):
    silnia= 1
    for j in range (1,i+1):
        silnia*=j
    if i%2 == 0:
        silnia *= -1
        gora += silnia
    if i%2 != 0:
        gora +=silnia
print(gora)
for i in range(1,n+1):
    dol1 += k
    k += 0.3
dol = round(dol1, 2)
print (dol)
print(round(gora/dol,2))