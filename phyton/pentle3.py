#Napisz program wyświetlający wszystkie liczby całkowite z przedziału od 50 do 100 podzielne przez dowolną liczbę k, którą podaje użytkownik. Przekształć program tak, aby przedział liczb podawał użytkownik.
print("Podaj k")
k = int(input())

for i in range (50, 100+1):
    w = i/k
    print (w)

