import math

cislo1 = int(input("zadej celé číslo"))
cislo2 = int(input("zadej druhé číslo"))
nvm = 0

print("co chceš s těmito čísli dělat?\n 1 = plus \n 2 = mínus\n 3 = krát\n 4 = děleno\n")

neco = int(input())

print("\n")

if neco == 1:
    nvm = cislo1 + cislo2
elif neco == 2:
    nvm = cislo1 - cislo2
elif neco == 3:
    nvm = cislo1 * cislo2
else:
    nvm = cislo1 / cislo2

print(nvm)


