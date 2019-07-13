import random
import time

print('''
    я подброшу монету 1000 раз.\n 
    Угадай сколько раз выпадет орёл.\n 
    Для продолжения нажми Enter
    ''')
input()

flips = 0
heads = 0
while flips < 1000:
    n = random.randint(0, 1)
    if n == 1:
        heads = heads + 1
    flips = flips + 1
    if flips == 900:
        time.sleep(3)
        print('при 900 бросках орёл выпал ' +str(heads)+ ' раз')
    if flips == 500:
        time.sleep(3)
        print('при 500 бросках орёл выпал ' +str(heads)+ ' раз')
    if flips == 100:
        time.sleep(3)
        print('при 100 бросках орёл выпал ' +str(heads)+ ' раз')
ans = input('Сколько орёл выпадет при 1000 бросках? ')
if ans == heads:
    time.sleep(3)
    print('Да ', end=' ')
else:
    time.sleep(3)
    print('Нет ', end=' ')
print('из 1000 бросков, орёл выпал ', heads, 'раз')
input('\nEnter')