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
            m = 'прекрасно'
        elif 5 <= unhappiness <= 10:
            m = 'неплохо'
        elif 11 <= unhappiness <= 15:
            m = 'плохо'
        else:
            m = 'ужасно'
        return m
    def talk(self):
        print('Меня зовут ', self.name, ' , я чувствую себя ', self.mood, ' сейчас.\n')
        self.__pass_time()
    def eat(self, food = 4):
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()
    def play(self, fun = 4):
        print('Уиии!')
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    crit_name = input('Имя зверюшки будет? ')
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
        choice = input('Выберите пункт меню ')
        if choice == '0':
            print('Пока')
        elif choice == '1':
            crit.talk()
        elif choice == '2':
            crit.eat()
        elif choice == '3':
            crit.play()
        else:
            print('нет такого пункта')
main()
input('\nEnter')