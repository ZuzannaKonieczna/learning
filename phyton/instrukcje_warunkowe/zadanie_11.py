#Napisz program obliczający pierwiastki równania kwadratowego.
import math 
a = int(input("Podaj współczynnik a: "))
b = int(input("Podaj współczynnik b: "))
c = int(input("Podaj współczynnik c: "))

if a > 0:
    delta = 0 
    delta = b*b - 4*a*c
    print("delta = ", delta)
    if delta < 0:
        x1 = -b - math.sqrt(delta)/2*a
        x2 = -b + math.sqrt(delta)/2*a
        print("Pierwszy pierwiastek: ", x1," Drugi pierwiastek: ", x2)
    elif delta == 0:
        x = - b / 2 *a
        print("Pierwiastek wynosi: ", x)
    else:
        print("Nie ma pierwiastków")