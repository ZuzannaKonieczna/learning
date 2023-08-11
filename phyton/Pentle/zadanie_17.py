#Napisz program sumujący wartości ciągu n liczb podawanych przez użytkownika. Ilość liczb podaje użytkownik jako pierwszą wartość.

n = int(input("Podaj n: "))
suma = 0
for i in range(0,n):
    x = int(input("Podaj x: "))
    suma+=x

print(suma)