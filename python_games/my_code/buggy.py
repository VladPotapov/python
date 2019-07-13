import random

num_1 = random.randint(1, 10)
num_2 = random.randint(1, 10)

print('сколько будет ' + str(num_1) + ' + ' + str(num_2) + '?')

answer = input()

if int(answer) == num_1 + num_2:
    print('верно')
else:
    print('нет, правильный ответ ' + str(num_1 + num_2))

input('\nEnter')