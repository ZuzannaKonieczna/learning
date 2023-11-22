n = int(input())
gora = 1
k = 2
dol = 1
l = -3
for i in range(1,n+1):
    gora *= k
    k += 0.5
for i in range (1, n+1):
    dol *= l
    l /= 10
print(gora)
print(dol)
wynik = gora/dol
print(wynik)