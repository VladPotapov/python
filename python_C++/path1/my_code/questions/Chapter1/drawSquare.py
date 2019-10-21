x1 = int(input('X1: '))
y1 = int(input('Y1: '))
x2 = int(input('X2: '))
y2 = int(input('Y2: '))

from graph import *

penColor('black')
brushColor('red')

rectangle(x1, y1, x2, y2)
run()