# -*- coding: utf-8 -*-
# игра Реверси
# version 1.0

import random
import sys

# размер игрового поля
WIDTH = 8
HEIGHT = 8

def drawBoard(board):
    # вывести игровое поле, 
    # переданное функции
    print('   12345678')
    print('  +--------+')

    for y in range(HEIGHT):
        print('%s|' % (y + 1), end='')
        
        for x in range(WIDTH):
            print(board[x][y], end='')

        print('|%s' % (y + 1))

    print('   12345678')
    print('  +--------+')

def getNewBoard():
    # создать структуру данных нового чистого игрового поля
    board = []
    
    for i in range(WIDTH):
        board.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
    
    return board

def isValidMove(board, tile, xstart, ystart):
    # false - если xstart, ystart недопустимый 
    # true - если ход допустим

    if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):
        return false

    if tile == 'X':
        otherTile = 'O'
    else:
        otherTile = 'X'

    tilesToFlip = []
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection #первый шаг в направлении x
        y += ydirection #первый шаг в направлении y
        while isOnBoard(x, y) and board[x][y] == otherTile:
            # продолжать двигаться в направлении x, y
            x += xdirection
            y += ydirection
            if isOnBoard(x, y) and board[x][y] == tile:
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tilesToFlip.append([x, y])

    # если ни одна из фишек не перевернулась, то ход недопустим
    if len(tilesToFlip) == 0:
        return False

    return tilesToFlip

def isOnBoard(x, y):
    # True если координаты есть на поле
    return x >= 0 and x <= WIDTH - 1 and y >= 0 and y <= HEIGHT - 1

def getBoardWithValidMoves(board, tile):
    # вернуть новое поле с допустимыми ходами
    bordCopy = getBoardCopy(board)

    for x, y in getValidMoves(boardCopy, tile):
        boardCopy[x][y] = '.'
    return boardCopy

def getValidMoves(board, tile):
    # список кординатов х, у с допустимыми ходами для игрока
    validMoves = []
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if isValidMove((board, tile, x, y) != False):
                validMoves.append([x, y])

    return validMoves

def getScoreOfBoard(board):
    # определить количество очков, посчитав фишки 
    # Вернуть словарь с ключами "Х" и "О"
    xscore = 0
    oscore = 0
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if board[x][y] == 'X':
                xscore += 1
            if board[x][y] == 'O':
                oscore += 1

    return {"X":xscore, "O":oscore}

    def enterPlayerTile():
        # выбор фишки для игрока
        # возворащает список с фишкой игрока
        # в качестве первого элемента и второго компютера

        tile = ''
        while not (tile == 'X' or tile == 'O'):
            print('Выберите X или O')
            tile = input().upper()

        if tile == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    def whoGoesFirst():
        # определить кто ходит первым
        if random.randint(0, 1) == 0:
            return "Koмпъютер"
        return "Человек"