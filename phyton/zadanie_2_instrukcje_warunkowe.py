"""
Napisz program informujący czy liczba podana przez użytkownika jest większa,
 mniejsza czy równa zero. Wykorzystaj tylko dwie instrukcje warunkowe.
"""
a = int(input("Podaj a: "))

if a < 0:
    print(f"{a} jest mniejsze od 0")
elif a == 0:
    print(f"{a} jest równe 0")
else:
    print(f"{a} jest wieksze od 0")