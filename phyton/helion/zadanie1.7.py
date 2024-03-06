def zad_a(n):
    a = -4
    for i in range(1,n+1):
        print("Zadanie a:", a)
        a += 3
def zad_b(n):
    a = -4
    for i in range(1,n+1):
        print("Zadanie b:", a)
        a += 3
        if a == 2 or a == 8 :
            a += 3

def zad_c(n):
    a = 12
    for i in range(1,n+1):
        print("Zadanie c:", a)
        a -= 4

def zad_d(n):
    a = 12
    for i in range(1,n+1):
        print("Zadanie d: ",a)
        a-= 4
        if a == 0:
            a -= 4

zad_a(7)
print("-------------------------------------")
zad_b(5)
print("----------------------------------")
zad_c(7)
print("----------------------------------")
zad_d(6)