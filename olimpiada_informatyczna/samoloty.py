def max_length_runway(n, m, airport):
    # Tworzymy listę, aby reprezentować lotnisko, gdzie 0 oznacza pole wolne, a 1 pole zajęte.
    airport_map = [[0 if airport[i][j] == '.' else 1 for j in range(n)] for i in range(n)]

    max_length = 0

    for i in range(n):
        for j in range(n):
            if airport_map[i][j] == 0:
                # Sprawdzamy poziome pasy startowe
                horizontal_length = sum(airport_map[i][j:min(j + m, n)])
                max_length = max(max_length, horizontal_length)

                # Sprawdzamy pionowe pasy startowe
                vertical_length = sum(airport_map[x][j] for x in range(i, min(i + m, n)))
                max_length = max(max_length, vertical_length)

    return max_length

# Wczytaj dane wejściowe
n, m = map(int, input().split())
airport = [input() for _ in range(n)]

# Oblicz i wypisz wynik
result = max_length_runway(n, m, airport)
print(result)
