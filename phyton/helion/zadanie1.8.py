def zadanie_a(n):
    góra = 2 * n
    suma = 0
    for i in range (1, n+1):
        suma = n + suma
    wynik = góra/suma
    return round(wynik,2)
def zadanie_b(n):
    suma = 0
    for i in range(1,n+1):
        dol = i*2
        suma = 1/dol + suma
    return round(suma,2)
def zadanie_c(n):
    iloczyn = 1
    for i in range(1,n+1):
        gora = i + 3
        iloczyn *= gora/n
    return round(iloczyn,2)
def zadanie_d(n):
    gora1 = 3
    suma = 0
    for i in range(1,n+1):
        gora = gora1 *2
        suma = suma + (gora/n)
        gora1 *=2
    return round(suma,2)

na = int(input("Podaj liczbę do a: "))
nb = int(input("Podaj liczbe do b: "))
nc = int(input("Podaj liczba do c: "))
nd = int(input("Podaj liczba do d: "))
print(zadanie_a(na))
print(zadanie_b(nb))
print(zadanie_c(nc))
print(zadanie_d(nd))
