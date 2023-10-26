from math import *
a = int(input("Podaj a:"))
b = int(input("Podaj b:"))
c = int(input("Podaj c:"))


if (a == 0):
    print("To nie jest równanie kwadratowe")
else:
    delta=b*b - 4*a*c
    ##print(delta)
    if(delta < 0):
        print("Nie ma pierwiastków")
    else:
        if (delta == 0):
            x = -b - sqrt(delta)/(2*a)
            print(x)
        else:
            x1 = (-b - sqrt(delta))/(2*a)
            x2 = (-b + sqrt(delta))/(2*a)
            print (x1, x2)