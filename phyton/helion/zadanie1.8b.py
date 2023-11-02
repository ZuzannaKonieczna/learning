n = int(input("Podaj n większe od 0: "))

if (n<=0):
    print("Liczba miała być większa od 0.")
else:
    sum = 0
    for i in range(n):
        d = i +1
        c = 1 / 2 * d
        print(c)
        sum += c
        print (sum)