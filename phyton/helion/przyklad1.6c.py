n = int(input("Podaj n: "))
a = -1
iloczyn = 1

for i in range(n):
    iloczyn *= a
    a *= -2
print(iloczyn)