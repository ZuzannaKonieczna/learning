#Napisz program pobierający od użytkownika liczbę całkowitą dodatnią. W przypadku podania liczby ujemnej lub zera, program prosi o podanie nowej wartości. Całość kończy się w momencie wprowadzenia liczby dodatniej.
print("Podaj liczbe dodatnia: ")
a =int(input())
while a<=0:
    print("To nie jest liczba dodatnia, podaj jeszcze raz")
    a = int(input())


