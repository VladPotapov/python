import sys

def open_file(file_name, mode):
	"""открыть файл"""
	try:
		the_file = open(file_name, mode, encoding='utf-8')
	except IOError as e:
		print("нет файла ",file_name, "\n")
		input("\n\nEnter")
		sys.exit()
	else:
		return the_file

def next_line(the_file):
	"""Возврат следующей строки из файла"""
	line = the_file.readline()
	line = line.replace("/", "\n")
	return line

def next_block(the_file):
	"""Возврат следующего блока данных из файла"""
	category = next_line(the_file)

	question = next_line(the_file)

	answers = []
	for i in range(3):
		answers.append(next_line(the_file))

	correct = next_line(the_file)
	if correct:
		correct = correct[0]

	explanation = next_line(the_file)

	cost = next_line(the_file)

	return category, question, answers, correct, explanation, cost

def welcome(title, name):
	print("\t\tДобро пожаловать в в викторину ", name, "\n")
	print("\t\t", title, "\n")

def main():
	trivia = open_file("trivia.txt", "r")
	name = input('Ваше имя? ')
	title = next_line(trivia)
	welcome(title, name)
	score = 0

	category, question, answers, correct, explanation, cost = next_block(trivia)
	# если первый блок есть
	while category:
		# задать вопрос
		print(category)
		print(question)
		for i in range(3):
			print("\t", i + 1, " - ",answers[i])

		answer = input("Выберите номер ответа ")

		if answer == correct:
			print("\nПравильно ", end=" ")
			score += int(cost)
		else:
			print("\nНеправильно ", end=" ")
		print(explanation)
		print("Счёт ", score, "\n\n")

		category, question, answers, correct, explanation, cost = next_block(trivia)

	trivia.close()

	print("Это был последний вопрос!")
	print("Ваш окончательный счёт ", score)

main()
input("\nВыход из игры")