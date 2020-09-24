try:
    num = float(input("Number: "))
except ValueError as e:
    print("Это не число")
    print(e)
else:
    import cards, games

class BJ_Hand(cards.Hand):
    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()

        if self.total:
            rep += "(" + str(self.total) + ")"

        return  rep
