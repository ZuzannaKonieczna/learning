n = int(input())
gora = 0
dol = 1
k = 2
for i in range(1,n+1):
    gora += i
for i in range (1,n+1):
    dol *= k
    k+=4

print(gora)
print(dol)

wynik = gora / dol 
print(wynik)