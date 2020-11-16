# -*- coding: utf-8 -*-
# personage
# нарисовать персонаж

from graph import *

x1, y1, x2, y2 = 50, 50, 300, 500
center_x = (x1 + x2) / 2
center_y = (y1 + y2) / 2


def frame(x1, y1, x2, y2, border, color):
    penColor(color)
    penSize(border)
    rectangle(x1, y1, x2, y2)


def head(x1, x2, y, r):
    center = (x1 + x2) / 2
    top = y + 100

    circle(center, top, r)

    # глаза
    circle(center - (center / 10), top - 10, r / 10)
    circle(center + (center / 10), top - 10, r / 10)

    # нос
    polygon([(center, top - 5), (center - 4, top + 15),
             (center + 4, top + 15), (center, top - 5)])

    # рот
    line(center - 10, top + 30, center + 10, top + 30)

# шея


def neck(x1, x2, w, h, top):
    center = (x1 + x2) / 2
    rectangle(center - w, top, center + w, top + h)

# туловище


def body(center_x, center_y, w, h):
    rectangle(center_x - (w / 2), center_y - (h / 2),
              center_x + (w / 2), center_y + (h / 2))

# руки


def arms(center_x, center_y, w, h):
    """руки персонажа"""
    line(
        center_x - (w / 2), center_y - (h / 2),
        center_x - (w / 2) * 2, center_y + (h / 2) - 15
    )
    line(
        center_x + (w / 2), center_y - (h / 2),
        center_x + w, center_y + (h / 2) - 15
    )


frame(x1, y1, x2, y2, 2, "grey")
head(x1, x2, y1, 40)
neck(x1, x2, 10, 30, 190)
body(center_x, center_y, 70, 115)
arms(center_x, center_y, 70, 115)
run()
