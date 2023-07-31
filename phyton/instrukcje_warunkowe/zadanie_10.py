#Napisz program sprawdzający czy z boków o długościach podanych przez użytkownika można zbudować trójkąt.

x = int(input("Podaj pierwszy bok: "))
y = int(input("Podaj drugi bok: "))
z = int(input("Podaj trzeci bok: "))

if (x + y > z) & (y + z > x) & (z + y > x):
    print("Można stworzyć trójkąt")
else:
    print("Nie można stworzyć trójkąta")