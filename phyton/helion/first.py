a = int(input("podaj a: "))
b = int(input("Podaj b: "))

if a !=0:
    x = -b/a
    print(x)
else:
    if (b==0):
        print("Nieskończenie wiele rozwiązań")
    else:
        print("Równanie sprzeczne")