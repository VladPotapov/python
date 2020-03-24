# -*- coding: utf-8 -*-

#alien blaster: version 2.0

import time
import random

def randNum():
    return random.randint(0, 1)


class Player(object):
    """игрок"""

    num = randNum()

    def caution(self, enemy):
        print("предупредительный выстрел")
        print('Немедленно покиньте зону земли')
        enemy.mockery()

    def blast(self, enemy):
        print("Игрок стреляет во врага")
        enemy.die(hero, invader)

class Alien(object):
    """Враждебный инопланетянен"""

    num = randNum()

    def die(self, play, ali):

        if play.num == ali.num:
            print("Ну вот и всё спета песенка моя")
            time.sleep(1)
            print("Передай моим личинкам живущим за 1000 световых лет")
            time.sleep(1)
            print("Что я их любил")
            time.sleep(1)
            print("А теперь прощай безжалостный мир")
        else:
            print("Ага промохнулся")
            time.sleep(1)
            print("Вот тебе получай")
            time.sleep(1)
            print("тюх-тюх, пах-пах, БАБАААХ!!!")

    def mockery(self):
        print('Ха-ха-ха, они думают что я испугаюсь их пуколок')

hero = Player()
invader = Alien()

def main():
    choice = None

    while choice != '0':
        print(
            """
            0 выход
            1 предупридительный выстрел
            2 стрелять на поражение
            """
        )

        choice = input('Выбор ')

        if choice == '0':
            print('Пока')
            break
        elif choice == '1':
            hero.caution(invader)
        elif choice == '2':
            hero.blast(invader)
            break

main()