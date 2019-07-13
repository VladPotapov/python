import sys, pickle
smeshariki = []

class Critter(object):
    total = 0

    @staticmethod
    def status():
        print("Сейчас зверюшек ", Critter.total)

    def __init__(self, name):
        print('Создан объект класса Critter')
        self.name = name
        Critter.total += 1

    def __str__(self):
        txt = "Объект класса Critter\n"
        txt += "Name: " +self.name+ "\n"
        txt += "Total: " +str(Critter.total)+ "\n"
        return txt



crit1 = Critter('Крош')
smeshariki.append(crit1)
crit2 = Critter('Ежидзе')
smeshariki.append(crit2)
crit3 = Critter('Лосяш')
smeshariki.append(crit3)
crit4 = Critter('Бараш')
smeshariki.append(crit4)
crit5 = Critter('Пин')
smeshariki.append(crit5)

Critter.status()

for i in range(len(smeshariki)):
    print(smeshariki[i])
input("\nEnter")