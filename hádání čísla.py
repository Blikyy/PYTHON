# HÁDÁNÍ ČÍSLA 

import random
import math

nejmensi = int(input("jake bude nejmensi cislo ?"))
nejvetsi = int(input("jake bude nejvetsi cislo ?"))

randomnumber = random.randint(nejmensi, nejvetsi)

print("mas jenom ", round(math.log(nejvetsi - nejmensi + 1, 2)), "pokusu\n")

pocet = 0

while pocet < math.log(nejvetsi - nejmensi + 1, 2):
    pocet += 1
    
    guess = int(input("uhadni cislo\n"))

    if guess == randomnumber:
        print("vyhral jsi\n")
    elif guess < randomnumber:
        print("moc male cislo\n")
    elif guess > randomnumber:
        print("moc velke cislo\n")
if pocet > math.log(nejvetsi - nejmensi + 1, 2):
    print("cislo bylo ", randomnumber)
    print("\npriste :)\n")


