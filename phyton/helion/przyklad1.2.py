import math

a = int(input())
b = int(input())
c = int(input())
if a == 0:
    exit()
else:
    b2 = b*b
    delta = b2 - 4*a*b
    if delta < 0:
        print("Nie ma rozwiązań")
    elif delta == 0:
        x1 = (-b + math.sqrt(delta))/ (2*a)
        print( round(x1,2))
    else:
        x2 = (-b - math.sqrt(delta))/(2*a)
        x3 = (-b + math.sqrt(delta))/(2*a)
        print(round (x2), round(x3))
