#Napisz program, który odpowiada na pytanie, czy wśród trzech liczb są choć dwie takie same.

x = int(input("Podaj x: "))
y = int(input("Podaj y: "))
z = int(input("Podaj z: "))

if x == y or y == z or x == z :
    print("W zbiorze są dwie takie same liczby")