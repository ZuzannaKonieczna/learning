#Napisz program wypisujący liczby naturalne parzyste od liczby podanej przez użytkownika do 0.
print("Podaj liczbe :")
x = int(input())

for i in range(x,-1, -1):
    if i%2==0:
        print(i)