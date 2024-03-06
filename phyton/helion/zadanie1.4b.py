import math

x = int(input("Podaj: "))

if x < 7 :
    y = (x ** 3)+1
elif x ==7 :
    y = x-1
elif x == 9 :
    y = math.sqrt(3 * x)
else:
    y = -8 * x
print(y)