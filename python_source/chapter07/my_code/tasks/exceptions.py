import sys, pickle, shelve
users = []

def open_file(file_name, mode):
    try:
        the_file = open(file_name, mode, encoding='utf-8')
    except IOError as e:
        print('Error: ', e)
        print('Нет файла', file_name, '\n')
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    line = the_file.readline()
    line = line.replace('|', '\n')
    return line

def next_block(the_file):
    question = next_line(the_file)
    correct = next_line(the_file)
    if correct:
#udalenie probela, chtobi pri vvode slova otvet bil pravilniy
        correct = correct.strip('\n')
    explanation = next_line(the_file)
    cost = next_line(the_file)
    return question, correct, explanation, cost

def welcome(title, name):
    print('\t\tДобро пожаловать в игру ',name, '\n')
    print('\t\t', title, '\n')

def next_user(x):
    try:
        user = pickle.load(x)
    except:
        print('конец игры')
    else:
        return user

def main():
    exc = open_file('exceptions.txt', 'r')
    name = input('Ваше имя? ')
    title = next_line(exc)
    welcome(title, name)
    score = 0
    question, correct, explanation, cost = next_block(exc)
    while question:
        print(question)
        answer = input('Выберите ответ ')
        if answer == correct:
            print('\nПравильно ', end=' ')
            score += int(cost)
        else:
            print('\nНеправильно ', end=' ')
        print(explanation)
        print('Счёт ', score, '\n\n')
        question, correct, explanation, cost = next_block(exc)
    exc.close()
    print('Это был последний вопрос')
    print('Ваш окончательный счёт ', score)

    user_score = [name, score]
    scores = open('exceptions_pickle.dat', 'ab')
    pickle.dump(user_score, scores)
    scores.close()

    file_exc = open('exceptions_pickle.dat', 'rb')
    the_user = next_user(file_exc)
    while the_user:
        users.append(the_user)
        the_user = next_user(file_exc)
    file_exc.close()

main()

s = shelve.open('exc_shelve.dat')
s['users'] = users
s.sync()

for i in s['users']:
    print(i)
s.close()
input('\nВыход из игры')