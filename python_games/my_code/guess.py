import random

guessesTaken = 0

print('Привет как тебя зовут? ')
myName = input()

number = random.randint(1, 20)

print('Что же ', myName, ' я загадал число от 1 до 20')

for guessesTaken in range(6):
	print('Попробуй угадать ')
	guess = input()
	guess = int(guess)
	if guess < number:
		print('Твоё число меньше')
	if guess > number:
		print('Твоё число больше')
	if guess == number:
		break
if guess == number:
	guessesTaken = str(guessesTaken + 1)
	print("Отлично ", myName, " тебе понадобилось всего ", guessesTaken, " попыток")

if guess != number:
	number = str(number)
	print('увы я загадал число ' + number)
input('\nEnter')