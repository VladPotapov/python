from graph import *

def fon():
    """фон программы"""
    brushColor('#f0f0f0')
    rectangle(20,20,480,550)

def windows():
    """вид окон программы"""
    brushColor('#ffffff')
    penColor('#828790')

    #первое окно
    rectangle(40,40,460,200)

    #второе окно
    rectangle(40,320,460,480)

def lines():
    """подчёркивание"""
    penColor("#dcdcdc")
    #window 1
    line(30,30,470,30)
    line(470,30,470,250)
    line(470,250,30,250)
    line(30,250,30,30)

    #window 2
    line(30,310,470,310)
    line(470,310,470,530)
    line(470,530,30,530)
    line(30,530,30,310)


def buttons():
    penColor("#adadad")
    brushColor("#e1e1e1")

    #buttons for one window
    #button 1
    rectangle(40,210,100,235)
    #button 2
    rectangle(120,210,180,235)

    #buttons for two window
    #button 1
    rectangle(40,490,100,515)
    #button 2
    rectangle(120,490,180,515)

def main():
    fon()
    windows()
    buttons()
    lines()
    run()

main()