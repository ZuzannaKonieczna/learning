def zad_c(n):
    k  =  - 1
    s = 1
    for i in range(n):
        s*=k
        k *=-2
        print (k, "suma:", s)
    return s
n = int(input("Podaj długość ciągu"))
print(zad_c(n))
