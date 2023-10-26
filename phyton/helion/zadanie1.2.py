a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if(a > b and a > c):
    print(a , "jest największe")
elif(b > a and b > c):
    print(b, "jest największe")
else:
    print(c, "jest największe")