from graph import *

def blue_hubcap():
    brushColor("blue")
    polygon([(50, 50), (110, 90), (95, 120), (75, 120)])
    circle(50, 50, 10)

def red_hubcap():
    brushColor("red")
    polygon([(120, 40), (95, 120), (140, 120)])
    circle(120, 40, 10)

def green_hubcap():
    brushColor("green")
    polygon([(190, 50), (133, 90), (140, 120), (160, 120)])
    circle(190, 50, 10)


def main():
    blue_hubcap()
    red_hubcap()
    green_hubcap()
    run()

main()