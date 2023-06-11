# Napisz program obliczający pole dowolnego trójkąta (dla boków a, b, c) wykorzystując wzór Herona.
import math

a = int(input("Podaj a "))
b = int(input("Podaj b "))
c = int(input("Podaj c "))

px = a + b + c
x = px/2

print("Pole trójkąta wynosi: ", math.sqrt(x*(x-a)*(x-b)*(x-c)))


