def silnia(n):
    if n == 0:
        return 1
    return silnia(n-1) * n 

n = int(input('Podaj n : '))

print('n! :', silnia(n))