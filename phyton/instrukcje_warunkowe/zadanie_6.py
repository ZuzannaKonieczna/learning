#Napisz program, który odpowiada na pytanie, czy trzy podawane liczby całkowite są ustawione w porządku rosnącym.

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))

if (a<b) & (b<c) :
    print ("Liczby zostały podane w porządku rosnącym!")
else:
    print("Liczby NIE zostały podane w porzadku rosnącym !")