import sys, pickle, shelve
users = []

def open_file(file_name, mode):
    try:
        the_file = open(file_name, mode, encoding='utf-8')
    except IOError as e:
        print('Error: ', e)
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
    for _ in range(3):
        answers.append(next_line(the_file))
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    explanation = next_line(the_file)
    cost = next_line(the_file)
    return category, question, answers, correct, explanation, cost

def welcome(title, name):
    print('Добро пожаловать в игру "Викторина" ', name)
    print(title)

def next_user(x):
    try:
        user = pickle.load(x)
    except:
        print('конец игры')
    else:
        return user

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
            print('\t ', i + 1, ' = ', answers[i])
        answer = input('Ваш ответ ')
        if answer == correct:
            print('\nПравильно ', end=' ')
            score += int(cost)
        else:
            print('\nНет ', end=' ')
        print(explanation)
        print('Счёт ', score, '\n')
        category, question, answers, correct, explanation, cost = next_block(trivia)
    trivia.close()
    print('Это был последний вопрос')
    print('ваш счёт ', score, ' очков')

    user_score = [name, score]
    scores = open('records_shelve.dat', 'ab')
    pickle.dump(user_score, scores)
    scores.close()

    file = open('records_shelve.dat', 'rb')

    the_user = next_user(file)
    while the_user:
        users.append(the_user)
        the_user = next_user(file)
    file.close()

main()

s = shelve.open('shelve.dat')
s['users'] = users
s.sync()

for i in s['users']:
    print(i)
s.close()
input('\nEnter')