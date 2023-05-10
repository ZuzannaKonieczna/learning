#Napisz program wyświetlający n kolejnych potęg liczby 2. Wartość n podaje użytkownik, musi to być liczba naturalna większa od 0.

print("podaj potege: ")
p = int(input())

l=1
for i in range(1,p+1):
    l=l*2

print(l)