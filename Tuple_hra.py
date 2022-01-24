import random
import os
import time

clear = lambda: os.system('cls')



myTuple = tuple(("BMW", "Audi", "Mercedes", "Volvo", "Nissan", "Mazda"))

computer = random.choice(myTuple)

print(*myTuple)
print("\n")

time.sleep(5)

clear()


count = 3

while count != 0:

    player = str(input("vyber zančku auta "))

    if player == computer:

        print("správně")
        break
    else:
        print("špatně")
        count -= 1

    if count == 0:
        print("Konec hry")
