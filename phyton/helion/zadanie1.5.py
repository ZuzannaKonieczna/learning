a = int(input("Podaj: "))
b = int(input("Podaj: "))
c = int(input("Podaj: "))

if a + b > c and  a + c > b and b + c > a:
    print("Może być")
else: print(" nie może")