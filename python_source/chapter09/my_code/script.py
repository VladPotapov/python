# Карты
# Демонстрирует сочетание объектов
# version 1.3

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


rank = input("Name rank: ")
while rank not in Card.RANKS:
    if rank == "exit" or rank == "выход":
        sys.exit()

    print("нет такой карты")
    print("ввдите другую, карту либо выход")
    rank = input("Name rank: ")

suit = input("Name suit: ")
while suit not in Card.SUITS:
    print("нет такой масти введите другую")
    suit = input("Name suit: ")

my_card = Card(rank, suit)


print(my_card)
