# простая игра
# Демонстрирует импорт модулей

import games, random

print("Добро пожаловать в игру")

again = None

while again != "n":
    players = []
    num = games.ask_number(question = "Сколько игроков учавствует? (2 - 5)", low = 2, high = 5)