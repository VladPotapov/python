# -*- coding: utf-8 -*-
import games, random

print("Добро пожаловать в игру")

again = None
while again != "n":
    players = []
    num = games.ask_number(que = "Сколько играков будет? (2 - 5) ", low = 2, high = 5)
    for i in range(num):
        name = input("Имя игрока: ")
        score = random.randrange(100) + 1
        player = games.Player(name, score)
        players.append(player)
    print("Результат игры:")
    for player in players:
        print(player)
    again = games.ask_yes_no("\nХотите сыграть ещё раз? (y/n): ")

input("\nEnter")