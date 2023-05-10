#Napisz program obliczający sumę liczb nieparzystych poczynając od liczby x, a kończąc na liczbie y
print ("podaj liczbe x")
x = int(input())
print ("podaj liczbe y")
y = int(input())
suma = 0
for i in range (x,y+1):
    if i % 2 != 0:
        suma = suma + i
        print (suma)
   