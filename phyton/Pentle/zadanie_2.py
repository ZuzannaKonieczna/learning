#Wyświetl przyste liczby całkowite z przedziału <2, 10>.

for liczba in range (2,11):
    if liczba % 2 == 0:
        print(liczba)


print("----------------------LUB-----------------------------")

for liczba in range (2,11,2):
    print(liczba)