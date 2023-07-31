#Napisz program, który dla zadanych dwóch liczb określi, czy pierwsza jest wielokrotnością drugiej.

a = int(input("Podaj a"))
b = int(input("Podaj b"))

if a % b == 0:
    print("Liczba ",a, "jest wielokrotnościa",b)
elif b % a == 0:
    print("Liczba ",b, "jest wielokrotnościa",a)
else:
    print("Żadna z liczb nie jest wielokrotością drugiej")