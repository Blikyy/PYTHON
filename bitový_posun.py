cislo = int(input("zadej cislo "))
bit = int(input("o kolik bitu "))
posun = int(input("1 = doleva 2 = doprava "))
lol = 0
if posun == 1:
    lol = cislo << bit
elif posun == 2:
    lol = cislo >> bit
    
print(lol)
