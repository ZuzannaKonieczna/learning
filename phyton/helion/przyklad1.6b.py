def zad_a(n):
    k = -4
    s = 0 
    for i in range(n):
        s += k
        k +=5
    return s

n = int(input("Podaj dłógość ciągu"))

print(zad_a(n))