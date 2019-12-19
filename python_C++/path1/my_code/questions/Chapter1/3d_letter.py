from graph import *

def letter_h():
    #top
    line(20, 50, 40, 50)
    line(80, 50, 100, 50)
    
    #left and right
    line(20, 50, 20, 150)
    line(100, 50, 100, 150)

    #bottom
    line(20, 150, 40, 150)
    line(80, 150, 100, 150)

    #internal sides - внутренние стороны
    line(40, 50, 40, 90)
    line(40, 110, 40, 150)
    line(80, 50, 80, 90)
    line(80, 110, 80, 150)

    #midst - середина
    line(40, 90, 80, 90)
    line(40, 110, 80, 110)
    line(45, 75, 80, 75)

def wrap_h():
    #top left
    line(25, 35, 45, 35)
    line(20, 50, 25, 35)
    line(40, 50, 45, 35)
    line(45, 35, 45, 75)
    line(40, 90, 45, 75)

    #top right
    line(85, 35, 105, 35)
    line(80, 50, 85, 35)
    line(100, 50, 105, 35)
    line(105, 35, 105, 135)
    line(100, 150, 105, 135)

    #bottom left
    line(40, 150, 45, 135)
    line(45, 135, 45, 110)

def letter_c():
    #left storana
    #verticalnaie
    line(150, 40, 150, 120)
    line(165, 70, 165, 115)
    line(200, 70, 200, 90)
    line(200, 135, 200, 150)

    #diagonal
    line(150, 40, 200, 70)
    line(165, 70, 200, 90)
    line(165, 115, 200, 135)
    line(150, 120, 200, 150)

def wrap_c():
    #right storona
    #verticalnie
    line(270, 40, 270, 60)
    line(250, 70, 250, 78)
    line(285, 100, 285, 115)

    #diagonal left
    line(150, 40, 220, 10)
    line(200, 70, 270, 40)
    line(200, 90, 270, 60)
    line(165, 115, 250, 78)
    line(200, 135, 285, 100)
    line(200, 150, 285, 115)

    #diagonal right
    line(220, 10, 270, 40)
    line(250, 78, 285, 100)


def main():
    letter_h()
    wrap_h()
    letter_c()
    wrap_c()
    run()

main()