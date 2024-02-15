n = int(input("Podaj n: "))
gora1 = n * n
silnie = [0] * (n+1)  
gora2 = [0] *(n+1)
gora3=1
dol1 = 0
dol2 = 0
for i in range(1, n+1):
    silnie[i] = 1
    for j in range(1, i+1):
        silnie[i] *= j
    gora2[i] = round(gora1/silnie[i],2)
    if i % 2 == 0:
        gora2[i] *= -1
    gora3 *= gora2[i]
for i in range(n):
    dol1 += 1
    dol2 += 3
    dol3 = round(dol1/dol2,2)
    print (dol1,"/", dol2 , "=",dol3)

for i in range(1, n+1):
    print(i,"! =",silnie[i])
    print(n ,"do kwadratu/",silnie[i],"=",gora2[i])

print(round(gora3/dol3,2))
    
