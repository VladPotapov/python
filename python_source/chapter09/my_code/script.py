# game blackjack
# version 1.0

import cards
import games


class BJ_Card(cards.Card):
    """Карта для игры"""
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1

            if v > 10:
                v = 10
        else:
            v = None

        return v


class BJ_Deck(cards.Deck):
    """колода для игры"""

    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))


class BJ_Hand(cards.Hand):
    """карты на руках игрока"""

    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()

        if self.total:
            rep += "(" + str(self.total) + ")"

        return rep

    @property
    def total(self):
        # если карта в руке имеет значение None, то total равен None
        for card in self.cards:
            if not card.value:
                return None

        # сложите значения карт, относитесь к каждому Тузу как к 1
        t = 0
        for card in self.cards:
            t += card.value

        # определите, содержит ли рука туза
        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True

        # если рука содержит туза и тотал достаточно низок, относитесь к Тузу как к 11
        if contains_ace and t <= 11:
            # добавьте только 10, так как мы уже добавили 1 для туза
            t += 10

        return t

    def is_busted(self):
        return self.total > 21


class BJ_Player(BJ_Hand):
    """Игрок"""

    def is_hitting(self):
        response = games.ask_yes_no(
            "\n" + self.name + ", будете брать карты? (y/n ")
        return response == "y"

    def bust(self):
        print(self.name, "перебрал. ")
        self.lose()

    def lose(self):
        print(self.name, "проиграл. ")

    def win(self):
        print(self.name, "выйграл. ")

    def push(self):
        print(self.name, "ничья.")


class BJ_Dealer(BJ_Hand):
    """Дилер"""

    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, "перебрал")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()


class BJ_Game(object):
    """"""
