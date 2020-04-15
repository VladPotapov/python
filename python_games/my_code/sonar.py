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