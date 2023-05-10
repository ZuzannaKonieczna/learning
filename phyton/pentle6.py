#Napisz program sumujący wartości ciągu n liczb podawanych przez użytkownika. Ilość liczb podaje użytkownik jako pierwszą wartość.

n = int(input("Podaj liczbe wyrazow w ciagu"))
suma = 0 

for i in range (0,n):
    m = int(input("Podaj liczbe "))
    suma += m
    print(suma)

print(suma)