n = int(input("Podaj n > 1: "))
g = 0
if n > 1 :
    for i in range(2, n):
        if n % i == 0:
            g += 1
if n == 2 or g == 0:
    print("Liczba pierwsza")
else:
    print("Liczba złozona")