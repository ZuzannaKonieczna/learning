import math

x = int(input())

if x < 1 :
    y = 2 * x
elif x == 1:
    y = -10
elif x == 3:
    y = x **4
elif x == 6 :
    y = math.sqrt(x - 4)
else:
    y = 0
print(y)