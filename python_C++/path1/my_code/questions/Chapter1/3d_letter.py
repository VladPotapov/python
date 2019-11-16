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

def wrap_h():
    #top left
    line(25, 35, 45, 35)
    line(20, 50, 25, 35)
    line(40, 50, 45, 35)
    line(45, 35, 45, 75)
    line(40, 90, 45, 75)

    #top right

def main():
    letter_h()
    wrap_h()
    run()

main()