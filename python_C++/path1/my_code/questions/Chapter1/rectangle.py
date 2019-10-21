#center rectangle
left = int(input("coordinat x: "))
top = int(input("coordinat y: "))

from graph import *

#size rectangle
w = 300
h = 100

#coordinats rectangle
rect_left = left - (w // 2)
rect_top = top - (h // 2)
rect_right = left + (w // 2)
rect_bottom = top + (h // 2)

rectangle(rect_left, rect_top, rect_right, rect_bottom)
run()

rect_lt = rect_left, rect_top
rect_lb = rect_left, rect_top + h
rect_rt = rect_right, rect_bottom - h
rect_rb = rect_right, rect_bottom

print(rect_lt, rect_rt, rect_rb, rect_lb)