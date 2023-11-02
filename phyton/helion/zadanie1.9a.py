n = int(input("Podaj n większe od 0: "))

if (n<=0):
    print("Liczba miała być większa od 0.")
else:
    k = -2
    sum = 0 
    for i in range (n):
        sum +=k
        
        if (k < 0):
            k= k*(-1)
            k +=3
        else:
            k +=3
            k = k*(-1)
       
    print(sum)