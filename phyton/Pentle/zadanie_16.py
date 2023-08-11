#Napisz program wyświetlający n kolejnych potęg liczby 2. Wartość n podaje użytkownik, musi to być liczba naturalna większa od 0.

n = int(input("Podaj n: "))
p=1
if n > 0:
    for i in range(1,n+1):
        p = p*2
        print(p)