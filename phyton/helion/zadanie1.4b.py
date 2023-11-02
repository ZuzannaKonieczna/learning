x = int(input())

if(x<7):
   y= x ** 3 - 1
elif (x == 7):
    y =x - 1
elif(x == 9):
    y = (3*x) ** (1/2)
else:
    y = -8*x

print(y)