#Napisz program sprawdzający czy liczba podana przez użytkownika jest z przedziału <1,10> lub <17,21>

x = int(input("Podaj x: "))

if (1<= x <=10) | (17<= x <=21):
    print("liczba należy do któregoś z przedziałów")
else: 
    print("Liczba nie należy do żadnego z przedziałów")