from graph import *
#попытка рисования за пределами холста приводит к зависанию
#или возможно к бесконечному циклу в попытке что-то нарисоват
#можно нарисовать линию уходящую за линию холста
#но не рисовать за пределами холста
line(5,2,5000,20)

line(10,20,10,15)

line(10,20,5,15)

line(10,20,15,20)

line(10,20,15,20)

penColor("red")
#если указать сначала правый верхний угол
#а потом левый нижний то функция всёравно сработает
rectangle(200,20,20,200)

#button
penColor('#e7e4e7')
brushColor('#efecef')
penSize('1')
line(300,75,300,50)
line(300,50,400,50)
penColor('#a5a2a5')
penSize('2.2')
line(400,50,400,75)
line(400,75,300,75)

#button click
penSize('1')
line(400,100,400,125)
line(400,125,300,125)
penColor('#e7e4e7')
brushColor('#efecef')
penSize('1')
line(300,125,300,100)
line(300,100,400,100)
run()