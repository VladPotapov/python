# -*- coding: utf-8 -*-

from graph import *

polygon([(10, 20), (10, 15), (10, 20), (5, 15), (10, 20), (15, 21), (10, 20), (15, 22)])
rectangle(150, 150, 50, 250)

#панель
brushColor("darkgray")
rectangle(300, 200, 400, 250)
#переключатель
brushColor("whitesmoke")
rectangle(300, 200, 350, 250)
brushColor("gray")
#значок
polygon([(315, 225), (325, 210), (320, 225), (325, 225), (319, 240), (320, 225)])
run()