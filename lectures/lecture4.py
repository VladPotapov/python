import graphics as gr
#-*- coding:utf-8 -*-
#Функции
#def hello(name) = формальный параметр
def hello(name="world"): #----параметр по умолчанию
    print('hello ', name)
#вызов
#hello()

#добавление функции в переменную
f = hello
#вызов через переменную
f('Romich')     #-----фактический параметр

#        _________ 
#   name |        |
#   -----|        |
#        |________|

def max2(x, y):
    if x > y:
        return x
    return y    #если y больше

n_max2 = max2(3,5)

#     _________
#   x | max2  |
#   --|       |---- max number
#   y |       |
#   --|       |
#     ---------

def max3(x,y,z):
    return max2(x, max2(y,z))
#           |           |
#вызов    второй      первый
#     _________
#   x | max3  |
#   --|       |
#   y |       |_____
#   --|       |
#   z |       |
#   --|       |
#     ---------

print(max3(17, 19, 2))
print(max3(1.5, 0.3, 17.9))
print(max3(1.3, 2.5,  17))

#Duck typing (утинный полиморфизм)
#сравнение происходит с помощью
#поиска большей буквы по алфавиту
#большим считается самое длинное слово
print(max3('ab','abc','abd'))
print(max2('кот','котёнок'))

#подчёркивание считается буквой

def hello_sepparated(name="world", sepparator="-"):
    print("hello ",name, sep=sepparator)

hello_sepparated(sepparator="***", name="Nike") #именнованный параметр

#Стэк вызовов (Call Stack)--
#-------                    |
#|main |- A - B - C - D |   B   |
#-------                |   A   |
#                       |  main |
#                       ---------

#Структурное программировани
#Проектирование сверху вниз

#Заказать дом
#  передаю параметры менджеру
#      где (window)
#      точка (upper_left_corner)
#      размер (width)
# 
# менеджер посылает параметры инженеру
# инженер посылает ответ менеджеру
# менеджер посылает ответ прорабу
# прораб посылает запрос на стройку
# прораб посылает
# менеджер посылает ответ тестировщику
# тестировщик возвращает true || false

#функция менеджер
def build_house(window, upper_left_corner, width):
    """функция которая рисует дом"""
    pass

window = gr.GraphWin("Russia game", 300, 300)

build_house(window, gr.Point(100, 100), 100)

print("Ура дом построен")

# Метод грубой силы (Brute force)
# обл. определ. --перебор--> массив значений

def is_simple_number(x):
    """
    является ли число x простым
    где x простое чичло
    да - True
    иначе - False"""
    divisor = 2
    while divisor < x:
        if x % divisor == 0:
            return False
        divisor += 1
    return True

def factorize_number(x):
    """
    Раскладывает число на множители
    печатает их на экран
    х - целое число положительное"""
    divisor = 2
    while x > 1:
        if x % divisor == 0:
            print(divisor)
            x //= divisor
        else:
            divisor += 1