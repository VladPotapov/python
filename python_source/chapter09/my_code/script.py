# Карты
# Демонстрирует сочетание объектов
# version 1.4

import sys


class Card(object):
    """ одна игральная карта """
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    # c трефы
    # d бубны
    # h червы
    # s пики
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep


class Hand(object):
    """Рука: набор карт игрока"""

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = "None cards"

        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


rank = "10"
while rank not in Card.RANKS:
    if rank == "exit" or rank == "выход":
        sys.exit()

    print("нет такой карты")
    print("ввдите другую, карту либо выход")
    rank = input("Name rank: ")

suit = "d"
while suit not in Card.SUITS:
    print("нет такой масти введите другую")
    suit = input("Name suit: ")

my_card = Card(rank, suit)

print(my_card)

try:
    print(my_card)
except NameError:
    print("Имя переменной или параметров не совпадают")


Djon = Hand()
Alen = Hand()

try:
    Djon.add("Qh")
except NameError:
    print("Нет такого игрока")
except AttributeError:
    print("Неправильно указан класс")
except TypeError:
    print("Не указана карта")
