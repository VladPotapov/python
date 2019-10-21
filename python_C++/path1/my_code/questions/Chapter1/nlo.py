from graph import *

def triangles():
    #первый триугольник
    penSize(0)
    brushColor("blue")
    polygon([(200, 20), (250, 50), (150, 50)])

    #второй триугольник
    brushColor("green")
    polygon([(150, 50), (250, 50), (200, 80)])

def circles():
    #первый круг
    brushColor("red")
    circle(125, 50, 25)
    brushColor("yellow")
    circle(275, 50, 25)

def nlo():
    triangles()
    circles()
    run()

nlo()