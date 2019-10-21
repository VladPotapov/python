house_x = int(input('Отступ слева '))
house_y = int(input('Отступ сверху '))

from graph import *

def roof(x, y):
    brushColor("blue")
    x_y_1 = (x + 150, y + 150)
    x_y_2 = (x + 225, y + 200)
    x_y_3 = (x + 75, y + 200)
    polygon([x_y_1, x_y_2, x_y_3])

def wall(x, y):
    brushColor("green")
    x_1 = x + 100
    y_1 = y + 200
    x_2 = x + 200
    y_2 = y + 300
    rectangle(x_1, y_1, x_2, y_2)

def house():
    roof(house_x, house_y)
    wall(house_x, house_y)



def main():
    house()
    run()

main()