n = int(input("Podaj n:"))
a = -4
suma = 0
for i in range(1,n+1):
    ##print(a)
    suma = suma + a
    a += 5

print(suma)