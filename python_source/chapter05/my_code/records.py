scores = []

choice = None

while choice != "":
	print(
		"""
		0 выход
		1 рекорды
		2 новый рекорд
		3 сортировать рекорды
		4 удалить рекорд
		5 показать в обратном порядке
		6 количество повторений рекорда
		7 узнать первый индекс рекорда
		8 вставить рекорд в индекс
		""")

	choice = input('выбрать пункт меню ')
	print()

	if choice == "0":
		print("пока")
		break

	elif choice == "1":
		print("Рекорды")
		for score in scores:
			print(score)

	elif choice == "2":
		score = int(input('новый рекорд '))
		scores.append(score)

	elif choice == "3":
		scores.sort(reverse=True)
		for score in scores:
			print(score)

	elif choice == "4":
		score = int(input('удалить рекорд '))
		if score in scores:
			scores.remove(score)
		else:
			print('нет такого рекорда')

	elif choice == "5":
		scores.reverse()
		for score in scores:
			print(score)

	elif choice == "6":
		score = int(input('выбрать рекорд '))
		count_score = scores.count(score)
		print('количество повторений ', count_score)

	elif choice == "7":
		score = int(input('выбрать рекорд '))
		print('первый индекс рекокрда ',scores.index(score))

	elif choice == "8":
		score = int(input('рекорд '))
		pos = int(input('позиция '))
		len_scores = len(scores) - 1
		if pos < len_scores or pos >= 0:
			scores.insert(pos, score)
		else:
			print('нет такой позиции')
	else:
		print('нет такого пункта')

input('\nEnter')