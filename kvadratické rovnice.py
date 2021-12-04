import math # přidám matematickou knihonnu

a = int(input("a"))
b = int(input("b"))
c = int(input("c"))
diskriminant = 0
x1 = 0
x2 = 0

# vytvořím proměnné

diskriminant = ((b**2) - (4 * a * c))
DiskriminantVar = math.sqrt(diskriminant)

# vypočítám diskriminant pomocí vzorce

if DiskriminantVar < 0:
    print("nemá řešení")
elif DiskriminantVar == 0:
    print("vysledek je nula")
else: 
    x1 = (-b + DiskriminantVar) / (2 * a)
    x2 = (-b - DiskriminantVar)  / (2 * a)

# podmínky 

print("vysledek x1 je", x1)
print("vysledek x2 je",x2)

# vypíšu pomocí std. výstupu :)