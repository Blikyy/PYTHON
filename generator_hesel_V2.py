import random

def shuffle(string):

    templist = list(string)
    random.shuffle(templist)
    return ''.join(templist)

lowercase1 = chr(random.randint(97, 122))
lowercase2 = chr(random.randint(97, 122))
lowercase3 = chr(random.randint(97, 122))

upercase1 = chr(random.randint(65, 90))
upercase2 = chr(random.randint(65, 90))
upercase3 = chr(random.randint(65, 90))

digit1 = chr(random.randint(48, 57))
digit2 = chr(random.randint(48, 57))
digit3 = chr(random.randint(48, 57))

specchar1 = chr(random.randint(33, 47))
specchar2 = chr(random.randint(58, 64))
specchar3 = chr(random.randint(91, 95))

password = lowercase1 + lowercase2 + lowercase3 + upercase1 + upercase2 + upercase3 + digit1 + digit2 + digit3 + specchar1 + specchar2 + specchar3
password = shuffle(password)

print(password)

with open('text.txt', 'w') as f:
    f.writelines(password)
