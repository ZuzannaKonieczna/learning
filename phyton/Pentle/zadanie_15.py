#Napisz program wypisujący liczby naturalne parzyste od liczby podanej przez użytkownika do 0.

x = int(input("Podaj x: "))

for liczba in range(x,0,-1):
    if liczba%2==0:
        print(liczba)