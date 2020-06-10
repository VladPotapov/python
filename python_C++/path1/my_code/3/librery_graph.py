# -*- coding: utf-8 -*-

from graph import *


def my_circle():
    i = 0
    x = 20
    y = 20
    z = 5
    while i < 3:
        circle(x, y, z)
        x += x
        y += y
        z += z
        i += 1


# размер окна
windowSize(500, 500)

# позволяет рисовать только в этой области
canvasSize(300, 300)
# указывает где будет область рисования
canvasPos(100, 50)

line(0, 20, 100, 20)

# проверяет находится ли пиксел в пределах windowsSize
point = pointInView(700, 5)

# если радиус выходит за пределы окна это False
circle = circleInView(250, 250, 20)

run()

print("pointInView ", point)
print("circleInView ", circle)
