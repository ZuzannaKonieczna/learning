a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))

p = (a + b + c )/2

p2 = p * (p-a) * (p-b) * (p-c)

if (p2 >0):
    pole = p2 * (1/2)
    print(pole)

