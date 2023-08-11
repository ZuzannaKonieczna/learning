#Napisz program wyświetlający wszystkie liczby całkowite z przedziału od 50 do 100 podzielne przez dowolną liczbę k, którą podaje użytkownik. Przekształć program tak, aby przedział liczb podawał użytkownik.

k = int(input("Podaj k: "))

for liczna in range (50,101):
    if liczna%k==0:
        print(liczna)