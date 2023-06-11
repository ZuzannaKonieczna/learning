#Napisz program obliczający obwód i pole trapezu równoramiennego.
a = int(input("Podaj pierwsza podstawe "))
b = int(input("Podaj druga podstawe "))
c = int(input("Podaj ramie "))
h = int(input("Podaj wyskosc"))

suma = a+b

print ( "Pole wynosi", suma * h /2)
print ("Obwód: ", suma + 2*h)