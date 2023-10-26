x = int(input("Podaj x: "))
y = int(input("Podaj y: "))

z = 5

x = x+2 

if(x < y):
    x = x*z
    y = y - 1 
elif (x == y ):
    y = y - z
    x = x - 1
else:
    y = y +z
    x = x + 1

print( "x =", x, "y= ", y)