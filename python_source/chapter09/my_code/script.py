# Карты
# Демонстрирует сочетание объектов
# version 1.2

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
suit = input("Name suit: ")


# разобраться с выходом из цикла
while rank not in Card.RANKS or suit not in Card.SUITS:
    print("Нет такой карты")
    rank = input("Name rank: ")
    suit = input("Name suit: ")
    if rank == "exit" or suit == "exit":
        break


while rank != False or suit != False:
    print("Вы не ввели данные")
    rank = input("Name rank: ")
    suit = input("Name suit: ")
    if rank == "exit" or suit == "exit":
        break
