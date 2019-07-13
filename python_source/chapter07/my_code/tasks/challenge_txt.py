import sys

def open_file(file_name, mode):
	try:
		the_file = open(file_name, mode, encoding='utf-8')
	except IOError as e:
		print('нет файла ', file_name, '\n')
		input('\nEnter')
		sys.exit()
	else:
		return the_file

def next_line(the_file):
	line = the_file.readline()
	line = line.replace('/', '\n')
	return line

def next_block(the_file):
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
	print('\nДобро пожаловать  в игру ', name)
	print(title)

def main():
	trivia = open_file('trivia.txt', 'r')
	name = input('\nName ')
	title = next_line(trivia)
	welcome(title, name)
	score = 0
	category, question, answers, correct, explanation, cost = next_block(trivia)
	while category:
		print(category)
		print(question)
		for i in range(3):
			print('\t', i + 1, ' = ', answers[i])
		answer = input('Выберите номер ответа ')
		if answer == correct:
			print('\nПравильно ', end=' ')
			score += int(cost)
		else:
			print('\nНеправильно', end=' ')
		print(explanation)
		print('Счёт ', score, '\n')
		category, question, answers, correct, explanation, cost = next_block(trivia)
	trivia.close()
	print('Это был последний вопрос')
	print('Ваш счёт ', score, ' очков')
	records = open_file('records_txt.txt', 'a')
	records.write(name)
	records.write('\t')
	records.write(str(score))
	records.write('\n')
	records.close()
	print('\nИтоги:')
	users = open_file('records_txt.txt', 'r')
	for user in users:
		print(user)
	users.close()
main()
input('\nВыход из игры')