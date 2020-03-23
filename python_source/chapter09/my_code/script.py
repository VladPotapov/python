# -*- coding: utf-8 -*-
import random
import time
class Player(object):
    #игрок
    def blast(self, enemi):
        print('Игрок стреляет во врага')
        time.sleep(1)
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        enemi.die()

class Alien(object):
    #пришелец
    def die(self):
        print('Пришелец: О нет меня подстрелили\n Как же так, я умираю')
        print('Я больше никогда не увижу своих миллионных потомков')
        print('Но они прилетят чтобы отомстить за меня вам людишки')

print('\t\t\t"ГИБЕЛЬ ПРИШЕЛЬЦА"')

hero = Player()
invaid = Alien()

hero.blast(invaid)

input("\nEnter")
