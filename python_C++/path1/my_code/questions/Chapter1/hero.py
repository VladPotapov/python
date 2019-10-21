#мой персонаж
from graph import *

#задний фон
def back_background():
    penColor('#fff')
    brushColor("#000")
    polygon([(10,100),(110,80),(210,100),(110,120),(10,100)])
#голова
def head():
    penColor('#000')
    brushColor('#fff')
    circle(110, 100, 30)
    line(90, 99, 95, 96)
    line(95, 96, 105, 102)
    line(115, 102, 125, 96)
    line(125, 96, 130, 99)

#головной убор
def cap():
    penColor('#000')
    brushColor('#000')
    polygon([(100, 10), (210, 99), (110, 79), (10, 99), (100,10)])

#борода
def beard():
    #правый ус
    polygon([(90, 115), (105, 112.5), (103, 117), (91, 116), (90.5, 145), (90, 115)])
    #левый ус
    polygon([(115, 112.5), (130, 115), (129.5, 145), (127.5, 115), (114, 116), (114, 115)])
    #борода
    polygon([(105, 120), (115, 120), (110, 145), (105, 120)])

def main():
    back_background()
    head()
    cap()
    beard()
    run()

main()