# -*- coding: utf-8 -*-

import tkinter as tk
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


def point_xy():
    x1 = 0
    y1 = 10
    penColor("blue")
    while x1 < 100:
        point(x1, y1)
        x1 += 1


def __keyPress(event):
    """показывает код нажатой буквы"""
    print("Key Press Event:")
    print(" event.char: ", event.char)
    print(" event.keysym: ", event.keysym)
    print(" event.keycode: ", event.keycode)
    print(" event.keysym_num: ", event.keysym_num)


point_xy()

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

# вывод кода клавиши
#root = tk.Tk()
#root.bind("<KeyPress>", __keyPress)
# tk.mainloop()
