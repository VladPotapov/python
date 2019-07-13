import random
import time

def displayIntro():
    print(
        '''
        Вы находитесь в землях, заселённых драконами
        Перед вами 2 пещеры, выберите одну из них
        В одной из них находится добрый дракон с сокровищами
        В другой злой и голодный, готовый вас сожрать
        '''
    )
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('В какую пещеру войдёте? ')
        cave = input()
    return cave

def checkCave(chosenCave):
    print('Вы приближаетесь к пещере...')
    time.sleep(2)
    print('Ее темнота заставляет вас дрожать от страха...')
    time.sleep(2)
    print('Большой дракон выпрыгивает перед вами и раскрыв свою пасть...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('...улыбаясь делится своими сокровищами')
    else:
        print('...съедает вас')


playAgain = 'да'

while playAgain == 'да' or playAgain == 'д':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    print('Попытаете удачу ещё раз? (да или нет)')
    playAgain = input()