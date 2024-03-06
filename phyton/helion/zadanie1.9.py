def a(n):
    suma = 0
    a = -2
    for i in range(1,n+1):
        suma += a
        if a < 0:
            a *= -1
            a += 3
        elif a > 0:
            a += 3
            a *= -1
    return suma
def b(n):
    a = 4
    iloczyn = 1
    for i in range(1,n+1):
        iloczyn *=a
        if a < 0:
            a *= -1
            a += 4
        elif a > 0:
            a += 4
            a *= -1
    return iloczyn

def c(n):
    iloczyn =1
    suma = 0
    for i in range(1,n+1):
        for j in range(1,i+1):
            iloczyn = 1
            iloczyn *= j
        suma += iloczyn
    return suma
def d(n):
    gora = 0
    dol = 1
    a = 2
    for i in range(1,n+1):
        gora += i;
        dol *= a
        a +=4
    wynik = gora/dol
    return round(wynik,2)

def e(n):
    gora = 1
    dol = 1
    a = 2
    b = -3
    for i in range(1,n+1):
        gora *= a
        a += 0.5
        dol *= b
        b *= 0.1
    wynik = gora/dol
    return round(wynik,2)
def f(n):
    gora = 0
    dol = 0
    a = -0.2
    for i in range(1,n+1):
        for j in range(1,i+1):
            iloczyn = 1
            iloczyn *= j
        if i%2 ==0:
            gora -= iloczyn
        else:
            gora += iloczyn
        dol += a
        a +=0.3
    wynik = gora / dol
    return round(wynik,2)
def g(n):
    gora = 0
    a = -2
    dol = 1
    b = 3
    for i in range(1,n+1):
        gora += a
        if a > 0:
            a +=5
            a *= -1
        elif a < 0:
            a *= -1
            a +=5
        dol *= b
        if b > 0:
            b += 4
            b *= -1
        elif b < 0:
            b *= -1
            b += 4

    wynik = gora /dol
    return round(wynik,2)
def h(n):
    gora = 1
    dol = 1
    a=1
    b =3
    for i in range(1,n+1):
        for j in range(1,i+1):
            iloczyn = 1
            iloczyn *= j
        if i%2 == 0:
            gora = gora * -1 * (n**2/ iloczyn)
        else:
            gora = gora *(n ** 2 / iloczyn)
        dol += a/b
        a += 1
        b += 3
    wynik = gora/dol
    return round(wynik,2)


menu = int(input("Który podpunkt chcesz sprawdzić: "))
n = int(input("Podaj:  "))
if menu == 1:
    print(a(n))
elif menu == 2:
    print(b(n))
elif menu == 3:
    print(c(n))
elif menu == 4:
    print(d(n))
elif menu == 5:
    print(e(n))
elif menu == 6:
    print(f(n))
elif menu == 7:
    print(g(n))
elif menu == 8:
    print(h(n))