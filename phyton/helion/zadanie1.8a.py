n = int(input("Podaj n większe od 0: "))

if (n<=0):
    print("Liczba miała być większa od 0.")
else:   
    c = 2 * n
    sum = 0
    for i in range(n):
        j = i+1
        sum+=j

    wynik = c / sum 

    print(wynik)