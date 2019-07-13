import random

chet  = 0
orel = 0
reshka = 0

while chet < 100:
    chet += 1
    money = random.randint(0,1)
    if money == 1:
        orel += 1
    else:
        reshka += 1
print('orel = ', orel)
print('oreshka = ', reshka)
input('\nEnter')