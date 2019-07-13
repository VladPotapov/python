# -*- coding: utf-8 -*-
import time
class Critter(object):
    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
    def __str__(self):
        setting_txt = "Настройки:\n"
        setting_txt += "Уровень голода " +self.hunger+ "\n"
        setting_txt += "Уровень скуки " +self.boredom+ "\n"
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1
    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = 'супер'
        elif unhappiness < 10:
            m = 'хорошо'
        elif unhappiness < 15:
            m = 'нормально'
        else:
            m = 'плохо'
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
            print('всё наелся')
        self.hunger -= self.food
        