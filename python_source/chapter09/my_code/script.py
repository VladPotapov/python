# Карты
# Демонстрирует сочетание объектов
# version 1.6

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


def check_rank(rank):
    while rank not in Card.RANKS:
        if rank == "exit" or rank == "выход":
            sys.exit()

        print("нет такой карты")
        print("ввдите другую, карту либо выход")
        rank = input("Name rank: ")

    if rank in Card.RANKS:
        return rank


def check_suit(suit):
    while suit not in Card.SUITS:
        if suit == "exit" or suit == "выход":
            sys.exit()

        print("нет такой масти введите другую")
        suit = input("Name suit: ")

    if suit in Card.SUITS:
        return suit


my_rank = input("Card: ")
check_rank(my_rank)
my_suit = input("Suit: ")
check_suit(my_suit)

card1 = Card(rank=my_rank, suit=my_suit)

my_rank = input("Card: ")
check_rank(my_rank)
my_suit = input("Suit: ")
check_suit(my_suit)

card2 = Card(rank=my_rank, suit=my_suit)

my_rank = input("Card: ")
check_rank(my_rank)
my_suit = input("Suit: ")
check_suit(my_suit)

card3 = Card(rank=my_rank, suit=my_suit)

my_rank = input("Card: ")
check_rank(my_rank)
my_suit = input("Suit: ")
check_suit(my_suit)

card4 = Card(rank=my_rank, suit=my_suit)

my_rank = input("Card: ")
check_rank(my_rank)
my_suit = input("Suit: ")
check_suit(my_suit)

card5 = Card(rank=my_rank, suit=my_suit)

try:
    print(card1)
except NameError:
    print("Имя переменной или параметров не совпадают")


Djon = Hand()
Djon.add(card1)
Djon.add(card2)

Alen = Hand()
Alen.add(card3)
Alen.add(card4)
Alen.add(card5)

try:
    Djon.add("Qh")
except NameError:
    print("Нет такого игрока")
except AttributeError:
    print("Неправильно указан класс")
except TypeError:
    print("Не указана карта")

print(Djon)
print(Alen)
