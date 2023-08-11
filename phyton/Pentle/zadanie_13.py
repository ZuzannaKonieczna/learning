#Napisz program obliczający sumę liczb nieparzystych poczynając od liczby x, a kończąc na liczbie y

x = int(input("Podaj x: "))
y = int(input("Podaj y: "))

suma=0
for liczba in range(x,y+1):
    if liczba%2==1:
        print(liczba)
        suma+=liczba

print("suma =", suma)