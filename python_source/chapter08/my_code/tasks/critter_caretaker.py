#если есть текст на русском
# -*- coding: utf-8 -*-
import time
class Critter(object):
    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1
    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = 'супер'
        elif 5 <= unhappiness <= 10:
            m = 'хорошо'
        elif 11 <= unhappiness <= 15:
            m = 'плохо'
        else:
            m = 'отвратительно'
        return m
    def talk(self):
        print('Имя: ', self.name, '\nСостояние: ', self.mood)
        self.__pass_time()
    def eat(self, food):
        self.food = food
        i = 0
        while i < self.food:
            time.sleep(1)
            print('хрум')
            i += 1
        if i == self.food:
            print('эээ')
            time.sleep(1)
            print('ааа')
        self.hunger -= self.food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()
    def play(self, fun):
        self.fun = fun
        i = 0
        arr = ["еху", "ух", "супер", "ещё", "ииияя", "вай как круто", "эге-ге", "смотри как я могу", "как круто", "ща сдохну"]
        while i < self.fun:
            time.sleep(1)
            print(arr[i])
            i += 1
        if i == self.fun:
            print('уф всё')
        self.boredom -= self.fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    crit_name = input('Имя для зверюшки ')
    crit = Critter(crit_name)
    choice = None

    while choice != '0':
        print(
            """
            0 выход
            1 узнать самочувствие
            2 покормить
            3 пойграть
            """
        )
        choice = input('выбрать пункт ')
        if choice == '0':
            print('Пока')
        elif choice == '1':
            crit.talk()
        elif choice == '2':
            crit_food = int(input('Введите число от 1 до 10 '))
            while crit_food < 0 or crit_food > 10:
                crit_food = input('Введите число от 1 до 10 ')
            crit.eat(crit_food)
        elif choice == '3':
            crit_fun = int(input('введите число от 1 до 10 '))
            while crit_fun < 0 or crit_fun > 10:
                crit_fun = int(input('введите число от 1 до 10 '))
            crit.play(crit_fun)
        else:
            print('нет такого пункта')

main()
input('\nEnter')