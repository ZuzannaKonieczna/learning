n = int(input("Podaj n większe od 0: "))

if (n<=0):
    print("Liczba miała być większa od 0.")
else:
    sum = 0 
    c = 3
    for i in range(n):
        c = 2 * c
        k = i + 1
        d = (c / k) 
        sum+= d
        
    print(sum)
