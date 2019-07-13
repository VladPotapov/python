# -*- coding: utf-8 -*-
import random
import time
class Animal():
    """
    Создаёт нового питомца
    Со своим номером и параметрами
    """
    #увеличивается при создание питомца
    total = 0
    #for hunger and boredom
    randomN1 = 0
    randomN2 = 0
    @staticmethod
    def status():
        print('Всего питомцев в зоопарке ', Animal.total)
    def __init__(self, name, number=0, hunger=0, boredom=0):
        self.name = name
        #номер питомца
        Animal.total += 1
        self.number = Animal.total
        Animal.randomN1 = random.randint(0,10)
        Animal.randomN2 = random.randint(0,10)
        #golod
        #присвает индивидуальные параметры 
        # для голода и скуки
        self.hunger = Animal.randomN1
        #skuka
        self.boredom = Animal.randomN2
    def __pass_time(self):
        """увеличивает уровень голода и скуки"""
        self.hunger += 1
        self.boredom += 1
    @property
    def mood(self):
        """Определяет уровеь самочуствия"""
        unhappiness = self.hunger + self.boredom
        if unhappiness <= 5:
            m = 'супер'
        elif unhappiness <= 10:
            m = 'хорошо'
        elif unhappiness <= 15:
            m = 'плохо'
        return m
    def __str__(self):
        information = 'Информация о животном\n'
        information += 'Имя ' +str(self.name)+ '\n'
        information += 'Питомец № ' +str(self.number)+ '\n'
        information += 'Уровень голода ' +str(self.hunger)+ '\n'
        information += 'Уровень скуки ' +str(self.boredom)+ '\n'
        return information
    def talk(self):
        print('Имя ', self.name, '\nСостояние ', self.mood)
        self.__pass_time()
    def eat(self, food):
        """покормить питомца"""
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
        delight = ["еху", "ух", "супер", "ещё", "ииияя", "вай как круто", "эге-ге", "смотри как я могу", "как круто", "ща сдохну"]
        while i < self.fun:
            time.sleep(1)
            print(delight[i])
            i += 1
        if i == self.fun:
            print('уф всё')
        self.boredom -= self.fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    print('Добро пожаловать в зоопарк')
    print('Вот наши питомцы')
    lion = Animal('Alex')
    zebra = Animal('Marty')
    hippo = Animal('Gloria')
    giraffe = Animal('Melman')
    
    print(lion)
    print(zebra)
    print(hippo)
    print(giraffe)

    Animal.status()

main()