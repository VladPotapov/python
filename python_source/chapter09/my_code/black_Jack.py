import cards, games

class BJ_Card(cards.Card):
    """карта для игры в блэк-джек"""
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
    """колода для игры в блэк-джек"""
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))

class BJ_Hand(cards.Hard):
    """Рука: набор карт у одного игрока"""
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
        for card in self.cards:
            if not card.value:
                return None

        t = 0

        for card in self.cards:
            t += card.value

        contains_ace = False

        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True

        if contains_ace and <= 11:
            t += 10

        return t

    def is_busted(self):
        return self.total > 21

class BJ_Player(BJ_Hand):
    def is_hitting(self):
        response = games.ask_yes_no("\n" +self.name+ " будете брать ещё карты? (Y/N): ")
        return response == "y"

    def bust(self):
        print(self.name, " перебрал")
        self.lose()

    def lose(self):
        print(self.name, " проиграл")

    def win(self):
        print(self.name, " выйграл")

    def push(self):
        print(self.name, " ничья")

class BJ_Dealer(BJ_Hand):
    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, " перебрал")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()

class BJ_Game(object):
    def __init__(self, names):
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)