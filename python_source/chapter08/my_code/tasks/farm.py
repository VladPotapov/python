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
    def game(self, fun):
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
    lion = Animal('Alex')
    zebra = Animal('Marty')
    hippo = Animal('Gloria')
    giraffe = Animal('Melman')
    animals = [lion, zebra, hippo, giraffe]
    print('Добро пожаловать в зоопарк')
    choice = None
    while choice != '0':
        print(
            """
            0 выход
            1 показать питомцев
            2 выбрать питомца
            3 покормить питомца
            4 пойграть с питомцем
            5 узнать состояние
            """
        )
        choice = input('выбрать пункт ')
        if choice == '0':
            print('до скорой встречи')
            break
        elif choice == '1':
            for i in range(len(animals)):
                print("Питомец № ", animals[i].number, " Имя ", animals[i].name)
        elif choice == '2':
            ans = int(input('показать зверюшку № '))
            while ans < 0 or ans > len(animals)-1:
                ans = int(input('показать зверюшку № '))
            print(animals[ans])
        elif choice == '3':
            food = int(input('Сколько еды вы хотите дать? от 0 до 10 '))
            while food < 0 or food > 10:
                food = int(input('Введите заново '))
            ans = int(input('какого питомца покормить? № '))
            while ans < 0 or ans > len(animals)-1:
                ans = int(input('какого питомца покормить? № '))
            animals[ans].eat(food)
        elif choice == '4':
            play = int(input('Сколько времени играть? от 0 до 10 '))
            while play < 0 or play > 10:
                play = int(input('Сколько времени играть? от 0 до 10 '))
            ans = int(input('Какого питомца выбрать? № '))
            while ans < 0 or ans > len(animals)-1:
                ans = int(input('Какого питомца выбрать? № '))
            animals[ans].game(play)
        elif choice == '5':
            ans = int(input('Какого питомца выбрать? № '))
            while ans < 0 or ans > len(animals)-1:
                ans = int(input('Какого питомца выбрать? № '))
            animals[ans].talk()
main()