#Wyświetl liczby całkowite z przedziału <x, y> (wartości x i y podaje użytkownik)


x = int(input("Podaj x: "))
y = int (input("podaj y : "))

for liczna in range (x, y+1):
    print(liczna)