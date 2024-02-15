def fib(n):
    if n == 1 or n == 2:
        return 1 
    return fib(n-1) + fib(n-2)

n = int(input('Podaj n:'))
print('lol:', fib(n))
