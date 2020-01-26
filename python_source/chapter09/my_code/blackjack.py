import cards, games

class BJ_Card(cards.Card):
    """карта для игры в блек-джек"""
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
    """Колода для игры"""
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))

class BJ_Hand(cards.Hand):
    """Набор карт у одного игрока"""
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
        # если у одной из карт свойство value равно None 
        # то всё равно None
        for card in in self.cards:
            if not card.value:
                return None

        # Суммируем очки. Считая каждый туз за 1 очко
        t = 0
        for card in self.cards:
            t += card.value

        # Проверяем есть ли туз
        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True

        # Если сумма очков не больше 11, то считаь туз за 11 очков
        if contains_ace and t <= 11:
            #прибавить 10, потому что 1 вошла в общую сумму
            t += 10

        return t

    def is_busted(self):
        return self.total > 21

class BJ_Player(BJ_Hand):
    """Игрок в Блэк-Джек"""
    def is_hitting(self):
        response = games.ask_yes_no("\n" + self.name + ", будете брать ещё карты? (y / n)")

        return  response == "y"

    def bust(self):
        print(self.name, "перебрал.")
        self.lose()

    def lose(self):
        print(self.name, "проиграл.")

    def win(self):
        print(self.name, "выйграл.") 

    def push(self):
        print(self.name, "ничья.")

class BJ_Dealer(BJ_Hand):
    """Диллер"""
    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, "перебрал")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()

class BJ_Game(object):
    """Игра в блэк-джек"""
    def __init__(self, names):
        self.players = []

        for name in names:
            player = BJ_Player(name)
            self.players.append(player)

        self.dealer = BJ_Dealer("Dealer")

        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()

        @property
        def still_playing(self):
            sp = []

            for player in self.player:
                if not player.is_busted():
                    sp.append(player)
            return sp

        def __additional_cards(self, player):
            while not player.is_busted() and player.is_hitting():
                self.deck.deal([player])
                print(player)

                if player.is_busted():
                    player.bust()

        def play(self):
            # сдать всем по 2 карты
            self.deck.deal(self.playrs + [self.dealer], per_hand = 2)
            # первая карта диллера переворачивается рубашкой вверх
            self.dealer.flip_first_card()

            for player in self.players:
                print(player)
            print(self.dealer)

            #сдача дополнительных карт
            for player in self.players:
                self.__additional_cards(player)

            self.dealer.flip_first_card()

            if not self.still_playing:
                # все игроки перебрали
                print(self.dealer)
            else:
                # сдача дополнительных карт диллеру
                print(self.dealer)
                self.__additional_cards(self.dealer)

                if self.dealer.is_busted():
                    # выигрывают все кто в игре
                    for player in self.still_playing:
                        player.win()