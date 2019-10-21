from graph import *
print('Рисуем квадрат')
a = 50
x = int(input('x = '))
y = int(input('y = '))
penColor('black')
brushColor('red')
rectangle(x,y,x+a,y+a)
polygon([(200,50), (300,100), (100,100), (200,50)])
run()