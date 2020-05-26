# -*- coding: utf-8 -*-

import games, random

print("Добро пожаловать в игру")

again = None
while again != "n":
    players = []
    num = games.ask_number(question = "Сколько человек будет играть (2 - 5)?: ", low = 2, high = 5)
    for i in range(num):
        name = input("Имя игрока: ")
        score = random.randint(100) + 1
        player = games.Player(name, score)
        players.append(player)

    print("Результат:")
    for player in players:
        print(player)

    again = games.ask_yes_no("\nХотите ещё раз сыграть? ")

input("\nEnter")