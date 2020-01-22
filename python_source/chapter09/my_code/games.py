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

def ask_yes_no(question):
    """задаёт вопрос с ответом да / нет"""
    res = None
    while res not in ("y", "n"):
        res = input(question).lower()
    return res

def ask_number(question, low, high):
    """просит ввести число из диапозона low, high"""
    res = None
    while res not in range(low, high):
        res = int(input(question))
    return res

if __name__ == "__main__":
    print("импортируйте модуль")
    input("\nEnter")