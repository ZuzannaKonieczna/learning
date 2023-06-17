#Napisz program wyznaczający najmniejszą z trzech liczb podanych przez użytkownika.

a = int(input("Podaj liczbe a:"))
b = int(input("Podaj b:"))
c = int(input("Podaj c:"))

print ("Najmniejsza jest:")
if a<b and a<c:
    print(f"{a}")
elif b<a and b<c :
    print(f"{b}")
else:
    print(f"{c}")