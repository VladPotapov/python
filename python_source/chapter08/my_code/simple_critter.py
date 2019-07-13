import random
hello_user = [
    'Привет, я твоя зверющка созданная с помощью класса Critter',
    'Привет чувак, ну чё давай потусуемся',
    'Ух ты, кого я вижу, ты ли это?',
    'О давно не виделись, ну как ты дружище?',
    'Ну наконец-то пришёл, я уж думал что с голоду подохну пока тебя жду'
]
"""выбор случайного приветствия"""
hello = random.choice(hello_user)
class Critter(object):
    def __init__(self, name):
        print('новая зверюшка созданная с помощью класса Critter')
        #добавляем имя для питомца
        self.name = name

    def __str__(self):
        rep = 'объект класса Critter\n'
        rep += 'имя ' + self.name + '\n'
        return rep

    def talk(self):
        print('Привет меня зовут ', self.name, '\n')

animal1 = Critter('Пятачёк')
animal1.talk()

print('Вывод объект animal1')
print(animal1)
print('Доступ к атрибуту animal1.name')
print(animal1.name)

animal2 = Critter('Хрюша')
animal2.talk()

print('Объект animal2')
print(animal2)
print('Доступ к атрибуту animal2.name')
print(animal2.name)

input('\nEnter')