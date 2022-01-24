import random
import string
zacatek = "https://prnt.sc/"
count = 1000
while count != 0:
    pismena = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(6))
    print(zacatek + pismena)
    count -= 1

