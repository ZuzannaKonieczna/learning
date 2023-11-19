def solve(n, m, buttons):
    row_count = [0] * n
    col_count = [0] * n

    for i in range(m):
        r, c = buttons[i]
        row_count[r - 1] += 1
        col_count[c - 1] += 1

    # Sprawdź warunek zadania
    if any(count % 2 != row_count[0] % 2 for count in row_count) or any(count % 2 != col_count[0] % 2 for count in col_count):
        print("NIE")
    else:
        print("TAK")
        k = sum(row_count)  # liczba aktywowanych p
        print(k)
        activated_buttons = [i + 1 for i in range(m) if row_count[buttons[i][0] - 1] % 2 == 1]
        print(" ".join(map(str, activated_buttons)))
n, m = map(int, input().split())

buttons = []
for i in range(m):
    r, c = map(int, input().split())
    buttons.append((r, c))
solve(n, m, buttons)
