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