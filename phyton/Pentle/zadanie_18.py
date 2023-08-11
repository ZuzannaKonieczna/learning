#Napisz program wyświetlający liczby całkowite z ciągu 0, 5, 15, 30, 50, 75, 105 … (wyświetl 10 pierwszych wartości)
liczba = 0
roznica = 5

for i in range(0,10):
    liczba+=roznica
    roznica+=5
    print(liczba)
    