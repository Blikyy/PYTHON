import random

misto = int(input("kolik míst bude mít heslo ?"))

for x in range(misto + 1):
    heslo = random.randint(48, 122)
    heslo = chr(heslo) 
    for nvm in heslo:
        print(heslo, end='')