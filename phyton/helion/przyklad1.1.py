a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
wynik = 0
if (a!= 0):
    wynik = -b/a
else:
    if(b==0):
        print("Nieskończenie wiele rozwiązań")
    else:
        print("Równanie sprzeczne")
print(wynik)