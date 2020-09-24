# -*- coding: utf-8 -*-
# задание 6 - нарисовать стандартное окно в операционной системе

from graph import *

penColor("Gray")
penSize(2)

# window
brushColor("LightSkyBlue")
rectangle(20, 20, 586, 324)

# buttons
brushColor("LavenderBlush")

rectangle(390, 20, 440, 58)
rectangle(390 + 5, 36, 440 - 5, 49)

rectangle(441, 20, 491, 58)
rectangle(441 + 5, 30, 491 - 5, 49)

brushColor("red")
x1 = 492
y1 = 20
x2 = 542
y2 = 58
x_center = (x1 + x2) / 2
y_center = (y1 + y2) / 2

rectangle(x1, y1, x2, y2)
brushColor("white")
penColor("white")
penSize(0)

Top1 = (x1 + 5, y1 + 5)
Top2 = (x2 - 5, y1 + 5)
Top3 = (x2 - 5, y1 + 7)
Top4 = (x1 + 5, y1 + 7)

bottom1 = (x2 - 5, y2 - 7)
bottom2 = (x2 - 5, y2 - 5)
bottom3 = (x1 + 5, y2 - 5)
bottom4 = (x1 + 5, y2 - 7)

centerTop = (x_center, y_center - 1)
centerBottom = (x_center, y_center + 1)
polygon([Top1, centerTop, Top2, Top3, centerBottom, bottom1, bottom2, centerBottom, bottom3, bottom4, centerBottom, Top4])
# canvas
penColor("black")
penSize(1)
rectangle(30, 70, 575, 310)


run()
