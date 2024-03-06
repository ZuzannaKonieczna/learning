n = int(input("Podaj ile liczb:"))
minimalna = 0
for i in range(1,n+1):
    k = int(input("Podaj liczbe:"))
    if k < minimalna or i == 1:
        minimalna = k
print(minimalna)
