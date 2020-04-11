#-*- coding: utf8
#playing cards
#version 1

class Card(object):
    """ игальная карта """
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    #clubs трефы
    #diamonds бубны
    #hearst червы
    #spades пики
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep

class Hand(object):
    """набор карт на руках у игрока"""
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = "<пусто>"
        
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

card1 = Card("A", "c")
card2 = Card("10", "s")
card3 = Card("Q", "c")
card4 = Card("7", "h")
card5 = Card("K", "d")

print("Вывод карт на экран")
print(card1)
print(card2)
print(card3)
print(card4)
print(card5)

my_hand = Hand()

print(my_hand)