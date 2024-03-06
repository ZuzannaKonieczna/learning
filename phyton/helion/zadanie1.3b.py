a = 3
b = -2
c = 10

if a+b <c:
    a *= 2
    b -= 1
    if c > 0 :
        c += a
    else:
        c += b
else:
    c += a*b

print(a,b,c)