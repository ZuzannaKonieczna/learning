    def generate_extended_word(n, S, k, a, b):
        licznik_litery = {}

        for i in range(n - k, n):
            litera = S[i]
            licznik_litery[litera] = licznik_litery.get(litera, 0) + 1

        posortowane_litery = sorted(licznik_litery.items())
        print(posortowane_litery)

        c = 0
        tab = [""] * (b - a + 1)

        for i in range(a, b + 1):
            tab[c] = posortowane_litery[c]
            c += 1

        for i in range(b + 1 - a):
            print(tab[i])

    n, k, a, b = map(int, input().split())
    S = input()

    generate_extended_word(n, S, k, a, b)
