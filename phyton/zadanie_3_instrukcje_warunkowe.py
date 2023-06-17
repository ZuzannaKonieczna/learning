#Napisz program informujący czy liczba podana przez użytkownika jest parzysta czy nieparzysta

a = int(input("Podaj x: "))
if a% 2 == 0:
    print(f"{a} jest parzyste")
else:
    print(f"{a} jest nieparzyste")