x = 5
y = 1
z = 6
x += y

if(x>y+1):
    x+=z
    z-=1 
if(z<3):
    z*=x
else:
    z*=y
    z+=1

print(x, y, z)