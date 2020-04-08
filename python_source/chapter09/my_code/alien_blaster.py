#-*- coding: utf-8 -*-
# version 2.1

import time
import random

def num():
    return random.randint(0, 1)

class Player(object):
    """игрок"""

    def caution(self, enemy):
        print("предупредительный выстрел")
        print('Немедленно покиньте зону земли')
        enemy.mockery()

    def blast(self, enemy):
        print("Игрок стреляет во врага")
        enemy.die()

class Alien(object):
    """Враждебный инопланетянен"""

    def die(self):
        print("Ну вот и всё спета песенка моя")
        time.sleep(1)
        print("Передай моим личинкам живущим за 1000 световых лет")
        time.sleep(1)
        print("Что я их любил")
        time.sleep(1)
        print("А теперь прощай безжалостный мир")

    def capture(self):
        print("промахнулся человечешка!")
        time.sleep(1)
        print("ну вот и настал твой конец тебе")
        time.sleep(1)
        print("и всем кто дорог тебе")
        time.sleep(1)
        print("А-ХА-ХА-ХА-ХА!!!")

    def mockery(self):
        print('Ха-ха-ха, они думают что я испугаюсь их пуколок')

def main():
    hero = Player()
    invader = Alien()

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
            if num() == num():
                hero.blast(invader)
            else:
                invader.capture()

main()