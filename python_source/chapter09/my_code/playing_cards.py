class Card(object):
    """игральная карта"""
    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    # diamons = бубны 
    # сlubs = трефы 
    # hearts = червы 
    # spades = пики
    SUITS = ['c', 'd', 'h', 's']

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep

class Hand(object):
    """список карт на руках"""
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

card1 = Card(rank = "A", suit = "c")
print(card1)

card2 = Card(rank = "2", suit = "c")
card3 = Card(rank = "3", suit = "c")
card4 = Card(rank = "4", suit = "c")
card5 = Card(rank = "5", suit = "c")
print(card1, ":", card2, ":", card3, ":", card4, ":", card5)

my_hand = Hand()
print("Карты которые у меня есть")
print(my_hand)

my_hand.add(card1)
my_hand.add(card2)
my_hand.add(card3)
my_hand.add(card4)
my_hand.add(card5)
print("Карты которые у меня есть")
print(my_hand)

your_hand = Hand()

my_hand.give(card2, your_hand)
my_hand.give(card5, your_hand)

print("Мои карты")
print(my_hand)
print("Ваши карты")
print(your_hand)

my_hand.clear()
print("Мои карты")
print(my_hand)

input("\nEnter")