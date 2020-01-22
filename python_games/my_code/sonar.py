# Охотник за сокровищами

import random
import sys
import math

def getNewBoard():
    """Создание игрового поля размером 60х15"""
    board = []
    # главный список из 60 списков
    for x in range(60):
        board.append([])
        # каждый список в главном списке 
        # содержит 15 односимвольных строк 
        # для создания океана используем разные символы, 
        # чтобы сделать его реалестичнее
        for y in range(15):
            if random.randint(0, 1) == 0:
                board[x].append('~')
            else:
                board[x].append('`')

    return board

def drawBoard(board):
    # Изобразить структуру данных игрового поля 
    # Создать место для чисел вниз по левой стороне поля
    tensDigitsLine = ' '

    for i in range(1, 6):
        tensDigitsLine += (' ' * 9) + str(i)

    # вывести числа в верхней части кода
    print(tensDigitsLine)
    print(' ' + ('0123456789' * 6))
    print()

    # вывести каждый из 15 рядов
    for row in range(15):
        # К однозначным числам нужно добавить дополнительный пробел
        if row < 10:
            extraSpace = ' '
        else:
            extraSpace = ''

        # Создать строку для этого ряда на игровом поле
        boardRow = ''
        for column in range(60):
            boardRow += board[column][row]

        print('%s%s %s %s' % (extraSpace, row, boardRow, row))

        # вывести числа в нижней части поля
        print()
        print(' ' + ('023456789' * 6))
        print(tensDigitsLine)

def getRandomChests(numChests):
    # Создать список структур данных сундука 
    # (двухэлементные списки целочисленных координат x,y)
    chests = []

    while len(chests) < numChests:
        newChests = [random.randint(0, 59), random.randint(0, 14)]

        if newChests not in chests:
            # убедиться что сундука тут нет
            chests.append(newChest)

    return chests

def isOnBoard(x, y):
    