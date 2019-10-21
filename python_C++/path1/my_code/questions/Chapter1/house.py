from graph import *
def roof():
    """крыша дома"""
    brushColor("blue")
    polygon([(150, 150), (225, 200), (225, 200), (75, 200)])

def wall():
    """стена дома"""
    brushColor("green")
    rectangle(100, 200, 200, 300)

def window():
    """окно дома"""
    penColor("white")
    brushColor("brown")
    penSize(3)
    rectangle(120, 220, 150, 270)
    line(120, 240, 150, 240)
    line(135, 240, 135, 270)

def house():
    """включает все пораметры для дома"""
    roof()
    wall()
    window()

def main():
    house()
    run()

main()