# -*- coding: utf-8 -*-
# version 2.0

import time
import random

def randNum():
    return random.randint(0, 1)

def yes_no(que):
    res = None

    while res not in ("y", "n", "д", "н"):
        res = input(que).lower()
    
    return res

def playGame(gamer):
    choice = None

    while choice != '0':
        print(
            """
            0 выход
            1 предупредительный выстрел
            2 стрелять на поражение
            """
        )

        choice = input('ваш выбор: ')

        if choice == '0':
            print('Пока')
            break
        elif choice == '1':
            gamer.caution(invader)
        elif choice == '2':
            gamer.blast(invader)
            break


class Player(object):
    """игрок"""
    def caution(self, enemy):
        print("предупредительный выстрел")
        print('Немедленно покиньте зону земли')
        enemy.mockery()

    def blast(self, enemy):
        print("Игрок стреляет во врага")
        enemy.die(hero, invader)

class Alien(object):
    """Враждебный инопланетянен"""

    def die(self, play, ali):

        # создать случайные числа и сравнить 
        # для выбора ответа
        if randNum() == randNum():
            print("Ну вот и всё спета песенка моя")
            time.sleep(1)
            print("Передай моим личинкам живущим за 1000 световых лет")
            time.sleep(1)
            print("Что я их любил")
            time.sleep(1)
            print("А теперь прощай безжалостный мир")
            print("Ура пришелец убит и мир может спать спокойно")
        else:
            print("Ага промохнулся")
            time.sleep(1)
            print("Вот тебе получай")
            time.sleep(1)
            print("тюх-тюх, пах-пах, БАБАААХ!!!")
            print("Увы, вы промахнулись и теперь весь мир обречён на гибель")

    def mockery(self):
        print('Ха-ха-ха, они думают что я испугаюсь их пуколок')

hero = Player()
invader = Alien()

def main():
    play = None
    while play != "n" or "н":
        playGame(hero)
        play = yes_no("Хотите сыграть ещё раз? д / н ")

main()