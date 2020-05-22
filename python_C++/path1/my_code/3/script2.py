# -*- coding: utf-8 -*-

x = int(input("Coordinat x: "))
y = int(input("Coordinat y: "))
a = int(input("size house: "))

from graph import *
rectangle(x, y, x + a, y + a)

run()