n = int(input("Podaj n większe od 0: "))

if (n<=0):
    print("Liczba miała być większa od 0.")
else:
    k = 4
    il = 1 
    for i in range (n):
        il *=k
        
        if (k < 0):
            k= k*(-1)
            k +=4
        else:
            k +=4
            k = k*(-1)
       
    print(il)