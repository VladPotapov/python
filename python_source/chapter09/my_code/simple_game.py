import games, random

print("Добро прожаловать в самую простую игру\n")
again = None

while again != "n":
    players = []
    num = games.ask_number(question = "сколько игроков учавствует? (от 2 до 5) ", low = 2, high = 5)
    
    for i in range(num):
        name = input('Имя ')
        score = random.randrange(100) +  1
        player = games.Player(name, score)
        players.append(player)

    print('Вот результаты\n')
    for player in players:
        print(player)

    again = games.ask_yes_no('хотите сыграть ещё раз? (y / n)')

input('\nEnter')