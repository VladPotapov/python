print('Ошибка IOError:')
print()
try:
	file = open('reads.txt', 'r', encoding='utf-8')
except IOError:
	print('нет такого файла')
	print()
else:
	print(file.read())
	file.close()

print('Ошибка IndexError:')
print()
arr = ['html', 'css', 'js', 'python']
try:
	arr_five = arr[5]
except IndexError:
	print('нет индекса 5 в кортеже')
	print()
else:
	print(arr_five)

print('Ошибка KeyError:')
print()
slovar = {
	'html':'дизайн сайта',
	'js':'скрипты',
	'php':'сервер'}
try:
	python = slovar['python']
except KeyError:
	print(slovar.get('python', 'нет ключа python в словаре'))
	print()
else:
	print(python)

print('Ошибка NameError')
print()
#name = 'Roman'
try:
	print(name)
except NameError:
	print('нет такого переменной или функции')
	print()

#придумать пример
print('Ошибка SyntaxError')
print()
try:
	name = "Roman"
except SyntaxError:
	print('ошибка в коде')
else:
	print(name)

print('Ошибка TypeError')
print()
try:
	primer = 'roman' + 3
except TypeError:
	print('вы пытаетесь сложить два разных типа')
	print()
else:
	print(primer)
	print()

print('Ошибка ValueError')
print()
try:
	num = int(input('введите число '))
except ValueError as e:
	print('это не число')
	#вывод ошибки от python
	print('error: ', e)
	print()
else:
	print('вы ввели число ', num)
	print()

print('Проверить 2 типа исключений')
print()
for value in (None, "Hello"):
	try:
		print('попытка преобразовать ', value, ' в число ', end=' ')
		print(float(value))
	except (TypeError, ValueError):
		print('Походу это не число')
input('\nEnter')