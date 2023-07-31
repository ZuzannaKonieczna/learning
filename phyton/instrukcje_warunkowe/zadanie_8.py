# Napisz program wyświetlający mniejszą z dwóch liczb podanych przez użytkownika. Jeżeli liczby są równe program wyświetla odpowieni komunikat.

x = int(input("Podaj x: "))
y = int(input("podaj y: "))

if x < y :
    print ( y, "Jest większe")
elif y < x:
    print(x, "jest większe")
else:
    print("Liczby są równe")