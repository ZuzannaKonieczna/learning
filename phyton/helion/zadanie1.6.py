import math

a = int(input("podaj a: "))
b = int(input("podaj b: "))
c = int(input("podaj c: "))

p = round((a+b+c)/2,2)

pod_pierwiastkiem = round(p * (p-a) * (p-b) * (p-c),2)

if pod_pierwiastkiem < 0:
    print("Error")
else:
    pole = round(math.sqrt(pod_pierwiastkiem),2)
    print("pole: ", pole)