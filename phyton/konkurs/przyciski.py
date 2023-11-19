def rozwiaz(n, m, przyciski):
    z = 0
    # Inicjalizacja list R i C
    R = [0] * n
    C = [0] * n

    # Licznik przycisków
    k = 0
    aktywowane_przyciski = []

    # Iteracja przez przyciski
    for i in range(m):
        ri, ci = przyciski[i]
        R[ri - 1] += 1  # Indeksowanie od 0
        C[ci - 1] += 1
        k += 1
        aktywowane_przyciski.append(i + 1)

    # Sprawdzenie parzystości
    parzyste_R = sum(x % 2 == 1 for x in R) % 2 == 0
    parzyste_C = sum(x % 2 == 1 for x in C) % 2 == 0

    if parzyste_R and parzyste_C:
        # Istnieje rozwiązanie
        print("TAK")
        print(k)
        print(" ".join(map(str, aktywowane_przyciski)))
        z += 1
    elif (not parzyste_R) and (not parzyste_C):
        # Istnieje rozwiązanie z jednym przyciskiem zamienionym
        for i in range(m):
            ri, ci = przyciski[i]
            if R[ri - 1] % 2 != C[ci - 1] % 2:
                # Zamień przycisk
                print("TAK")
                print(1)
                print(i + 1)
                z += 1
                return

    if z == 0:
        print("NIE")

# Przykład użycia
n, m = map(int, input().split())
przyciski = [list(map(int, input().split())) for _ in range(m)]

rozwiaz(n, m, przyciski)
