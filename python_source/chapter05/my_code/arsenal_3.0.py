inventory = ["меч", "щит", "шлем", "кольчуга", "целебное снадобье"]
for i in inventory:
	print(i)
print('сейчас у вас ', len(inventory), ' предметов')
if 'целебное снадобье' in inventory:
	print('есть чем раны зализать')
start = int(input('\nStart: '))
finish = int(input('\nFinish: '))
if finish > len(inventory):
	print('нет индекса ', finish)
else:
	print(inventory[start:finish])
chest = ["золото", "драгоценные камни"]
print("\nвы нашли")
print(chest)
inventory += chest
print('теперь в вашем арсенале')
for i in inventory:
	print(i)
inventory[0] = 'арбалет'
print('вы решили обменять меч на ', inventory[0])
inventory[4:6] = ['магический кристалл']
print('\nтеперь в арсенале')
for i in inventory:
	print(i)
print("\nв тяжолом бою был раздолблен ваш щит")
del inventory[1]
print('\nУ вас осталось')
print(inventory)
print('Так же у вас украли шлем и арбалет')
del inventory[:2]
print('вот всё что у вас осталось')
for i in inventory:
	print(i)
print('а ещё кто-то стырил драгоценные камни')
del inventory[len(inventory)-1]
print('и в итоге вот всё что осталось')
print(inventory)
input('\nEnter')