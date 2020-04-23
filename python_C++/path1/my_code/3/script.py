# -*- coding: utf-8 -*-

from graph import *

# цвет
penColor("white")
# попиксельно
point(10, 20)
penColor("black")
point(12, 21)
penColor("gray")
point(13, 22)
penColor("navy")
point(14, 23)
penColor("blue")
point(15, 24)
penColor("cyan")
point(16, 26)
penColor("green")
point(17, 27)
penColor("yellow")
point(18, 28)
penColor("red")
point(19, 29)
penColor("orange")
point(20, 30)

penColor("black")
penSize(3)
# рисует только прямые линии
line(10, 50, 30, 50)
penColor("navy")
line(10, 60, 30, 60)
penColor("cyan")
line(10, 70, 30, 70)
penColor("maroon")
line(10, 80, 30, 80)
penColor("violet")
line(10, 90, 30, 90)
penColor("purple")
line(10, 100, 30, 100)

# дом с помощью line
# стена
penColor("black")
line(50, 50, 150, 50)
line(150, 50, 150, 100)
line(150, 100, 50, 100)
line(50, 100, 50, 50)

penColor("brown")
penSize(20)
line(80, 70, 80, 100)

# окно
line(120, 60, 120, 80)

# дом с помощью polygon
penSize(2)
penColor("black")
#крыша 
polygon([(200, 50), (250, 25), (300, 50)])
# стена
polygon([(200, 50), (300, 50), (300, 100), (200, 100), (200, 50)])
# дверь
penColor("maroon")
penSize(2)
polygon([(220, 100), (220, 70), (240, 70), (240, 100)])
# окно
polygon([(260, 60), (280, 60), (280, 80), (260, 80), (260, 60)])

# крыша 
polygon([(50, 300), (75, 275), (175, 275), (200, 300), (50, 300)])
# стена 
rectangle(60, 300, 190, 350)
# окна  
x1 = 70
y1 = 310
x2 = 90
y2 = 330
for _ in range(4):
    rectangle(x1, y1, x2, y2)
    x1 += 30
    x2 += 30
# дверь

run()