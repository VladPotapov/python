import random

def drawBoard(board):
    """выводит на экран игровое поле"""
    print(board[7]+ '|' +board[8]+ '|' +board[9])
    print('-+-+-')
    print(board[4]+ '|' +board[5]+ '|' +board[6])
    print('-+-+-')
    print(board[1]+ '|' +board[2]+ '|' +board[3])

def inputPlayerLetter():
    """разрешенние ввести букву"""

    #возвращает массив
    letter = ''
    
    while not (letter == 'X' or letter == 'O'):
        print('Вы вибираете X или O')
        letter = input().upper()

    #первый элемент буква игрока, вторая компа
    if letter == 'X':
        return ['X', '0']
    else:
        return ['O', 'X']

def whoGoesFirst():
    """случайный выбор игрока, который ходит первым"""
    if random.randint(0, 1) == 0:
        return 'Компьютер'
    else:
        return 'Игрок'

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    """
        Учитывает заполнение игрового поля
        Возвращает True если игрок выйграл
    """
    return (
        (bo[7] == le and bo[8] == le and bo[9] == le) or 
        (bo[4] == le and bo[5] == le and bo[6] == le) or 
        (bo[1] == le and bo[2] == le and bo[3] == le) or 
        (bo[7] == le and bo[4] == le and bo[1] == le) or 
        (bo[8] == le and bo[5] == le and bo[2] == le) or
        (bo[9] == le and bo[6] == le and bo[3] == le) or
        (bo[7] == le and bo[5] == le and bo[3] == le) or
        (bo[9] == le and bo[5] == le and bo[1] == le)
    )

def getBoardCopy(board):
    """создаёт копию игрового поля"""
    boardCopy = []

    for i in board:
        boardCopy.append(i)
        return boardCopy

def isSpaceFree(board, move):
    """Возвращает True если ход сделан на свободное поле"""
    return board[move] == ''

def getPlayerMove(board):
    """разрешение игроку сделать ход"""
    move = ''