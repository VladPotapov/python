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
    return board[move] == ' '

def getPlayerMove(board):
    """разрешение игроку сделать ход"""
    move = ''

    while move not in '1 2 3 3 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('Ваш ход от 1 до 9? ')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []

    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])

    if move != None:
        return move
    
    if isSpaceFree(board, 5):
        return 5

    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

print('Игра "Крестики-Нолики"')

while True:
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('' + turn + ' ходит первым')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'Человек':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Ура вы выйграли')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Ничья')
                    break
                else:
                    turn = 'Компьютер'
        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('Компьютер победил')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Ничья')
                    break
                else:
                    turn = 'Человек'

    print('Сыграем ущё раз (да или нет)')
    if not input().lower().startswith('д'):
        break