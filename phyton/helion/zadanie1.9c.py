n = int(input("Podaj n większe od 0: "))

if n <= 0:
    print("Liczba miała być większa od 0.")
else:
    product = 0
    for i in range(1, n + 1):  # start from 1 to include n in the range
        factorial = 1
        for j in range(1, i + 1):  # start from 1 to include i in the range
            factorial *= j
        product += factorial
        print (i, product)

print(f"Iloczyn silni od 1 do {n} wynosi: {product}")
