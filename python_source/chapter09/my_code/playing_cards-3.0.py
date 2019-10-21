class Card():
    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    SUITS = ['c', 'd', 'h', 's']

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep

class Unpritable_Card(Card):
    def __str__(self):
        return "<карты скрыты от просмотра>"

class Positionable_Card(Card):
    def __init__(self, rank, suit, face_up = True):
        super(Positionable_Card, self).__init__(rank, suit)
        self.is_face_up = face_up
    
    def __str__(self):
        if self.is_face_up:
            rep = super(Positionable_Card, self).__str__()
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up

card1 = Card("A", "c")
card2 = Unpritable_Card("A", "d")
card3 = Positionable_Card("A", "h")

print("Object Card", end=" ")
print(card1)
print("Object Unpritable_Card", end=" ")
print(card2)
print("Object Positionable_Card", end=" ")
print(card3)
card3.flip()
print(card3)
input('\nEnter')