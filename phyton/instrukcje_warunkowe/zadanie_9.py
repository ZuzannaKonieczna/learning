#Napisz program informujący czy liczba podana przez użytkownika jest większa, mniejsza lub równa zero.

x = int(input("Podaj x: "))

if x == 0 :
    print("Liczba równa zero")
elif x < 0:
    print("Liczba", x, "jest mniejsza od zera")
else:
    print("Liczba", x, "jest wieksza od zera")