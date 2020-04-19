# -*- coding: utf-8 
# sonar.py 
# version 1.0

import random
import sys
import math

def getNewBoard():
    # создать структуру  данных нового игрового поля размером 60х15
    board = []
    for x in range(60): # главный список из 60 списков
        board.append([])
        for _ in range(15): # каждый список в главном списке содержит 15 односимвольных строк 
            # для создания океана испльзуем разные символы, чтобы сделать его реалистичнее
            if random.randint(0, 1) == 0:
                board[x].append('~')
            else:
                board[x].append('`')
    return board

def drawBoard(board):
    # изобразить структуру данных игрового поля
    tensDigitalsLine = ' '  # создать место для чисел вниз по левой стороне поля
    for i in range(1, 6):
        tensDigitalsLine += (' ' * 9) + str(i)

    # вывести числа в верхней части поля
    print(tensDigitalsLine)
    print(' ' + ('0123456789' * 6))
    print()

    # вывести каждый из 15 рядов
    for row in range(15):
        # к однозначным числам нужно добавить дополнитльный пробел
        if row < 10:
            extraSpace = ' '
        else:
            extraSpace = ''

        # создать строку для этого игрового ряда на игровом поле
        boardRow = ''
        for column in range(60):
            boardRow += board[column][row]

        print('%s%s %s %s' % (extraSpace, row, boardRow, row))

    # вывести числа в нижней части тела
    print()
    print(' ' + ('0123456789' * 6))
    print(tensDigitalsLine)

def getRandomChests(numChests):
    # создать список структур данных сундука (двухэлемнтыные списки координат х, у)
    chests = []
    while len(chests) < numChests:
        newChests = [random.randint(0, 59), random.randint(0, 14)]
        if newChests not in chests: # убедится что сундука тут нет
            chests.append(newChests)
    return chests

def isOnBoard(x, y):
    # возвращать true если координаты есть на поле, иначе возвращать false
    return  x >= 0 and x <= 59 and y >= 0 and y <= 14

def makeMove(board, chests, x, y):
    #изменить структуру поля данных поля, используя символ гитдролокатора. 
    # Удалить сундуки из списка если они найдены. 
    # Вернуть False это недопустимый ход 
    # Иначе вернуть строку с результатами хода 
    # Все сундуки будут расположены ближе, 
    # чем на растоянии в 100 единиц
    smallestDistance = 100
    for cx, cy in chests:
        distance = math.sqrt((cx - x) * (cx - x) + (cy - y) * (cy - y))

        #ищем ближайший сундук
        if distance < smallestDistance:
            smallestDistance = distance

    smallestDistance = round(smallestDistance)

    if smallestDistance == 0:
        # координаты xy указывают на сундук
        chests.remove([x, y])
        return "Вы нашли сундук с сокровищами на затонувшем судне"
    else:
        if smallestDistance < 10:
            board[x][y] = str(smallestDistance)
            return  "Сундук с сокровищами обнаружен на растоянии %x от гидролокатора." % (smallestDistance)
        else:
            board[x][y] = 'x'
            return  'Гидролокатор ничего не обнаружил'

def enterPlayerMove(previousMoves):
    #позволить игроку сделать ход. 
    # Вернуть двухэлементный список с целыми координатами x, y
    print(
        """
        Где следует опустить гидролокатор (координаты 
        x: (0 - 59), y: (0 - 14)
        или введите выход
        """
    )

    while True:
        move = input()
        if move.lower() == "выход":
            print("Спасибо за игру")
            sys.exit()

        move = move.split()
        if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and isOnBoard(int(move[0]), int(move[1])):
            #....