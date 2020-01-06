#Игры
#Демонстрирует создание модуля

class Player(object):
    """Участник игры"""
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score

    def __str__(self):
        rep = self.name + ":\t" + str(self.score)
        return rep

def ask_yes_no(que):
    """задаёт вопрос с ответом да / нет"""
    res = None
    while res not in ("y", "n"):
        res = input(que).lower()
    return res

def ask_number(que, low, high):
    """просит ввести число из диапозона low, high"""
    res = None
    while res not in range(low, high):
        res = int(input(que))
    return res

if __name__ == "__main__":
    print("импортируйте модуль")
    input("\nEnter")