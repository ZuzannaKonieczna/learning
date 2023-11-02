x = int(input("podaj 1 bok "))
y = int(input("podaj 2 bok "))
z = int(input("podaj 3 bok "))




if (x + y > z and x + z > y and z + y > x):
    print("Możana stworzyć trójkat ")
else:
    print("Nie może być trójkątem ")
