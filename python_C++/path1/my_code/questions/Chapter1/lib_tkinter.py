#import tkinter = error
from tkinter import *

#виджет combobox выпадающий список
from tkinter.ttk import Combobox
#checkbox
from tkinter.ttk import Checkbutton
#radio
from tkinter.ttk import Radiobutton

#текстовое поле большого размера
from tkinter import scrolledtext

def clicked():
    hello.configure(text = "Привет {}".format(txt.get()))
    

window = Tk()
#заголовок
window.title("Добро пожаловать в приложение Python")
#размер окна
window.geometry('600x350')

#текст в окне
lbl = Label(window, text="Привет", font=("Arial Bold", 50))
#расположение элемента
lbl.grid(column = 0, row = 0)

#ввод текста
txt = Entry(window, width = 25)
txt.grid(column = 1, row = 0)
#фокус ввода
txt.focus()

ans = Label(window, text = "Выбрать ")
ans.grid(column = 0, row = 3)


#выподающий список
combo = Combobox(window)
#значения
combo['values'] = (1, 2, 3, 4, 5, "text")
#значение по умолчанию
combo.current(5)
combo.grid(column = 1, row = 3)

clr = Label(window, text = "ваш любимый цвет?")
clr.grid(column = 0, row = 4)

#checkbox
chk_state = BooleanVar()
#vibor po umolchaniyu
chk_state.set(True)
chk1 = Checkbutton(window, text = "red", var = chk_state)
chk1.grid(column = 0, row = 5)

chk_state2 = IntVar()
chk_state2.set(1)
chk2 = Checkbutton(window, text = "green", var = chk_state2)
chk2.grid(column = 1, row = 5)

chk3 = Checkbutton(window, text = "blue")
chk3.grid(column = 2, row = 5)

lang = Label(window, text = "какой язык круче?")
lang.grid(column = 0, row = 6)

#radio, variable peredaet znachenie
selected = IntVar()
rad1 = Radiobutton(window, text = "js", value = 1, variable = selected)
rad2 = Radiobutton(window, text = "python", value = 2, variable = selected)
rad3 = Radiobutton(window, text = "c++", value = 3, variable = selected)
rad1.grid(column = 0, row = 7)
rad2.grid(column = 1, row = 7)
rad3.grid(column = 2, row = 7)

#about
txt_about = Label(window, text = "Раскажите о себе")
txt_about.grid(column = 0, row = 8)
about = scrolledtext.ScrolledText(window, width = 40, height = 5)
about.grid(column = 0, row = 9)

hello = Label(window, text = "")
hello.grid(column = 0, row = 10)

btn = Button(window, text = "click me", command = clicked)
btn.grid(column = 0, row = 11)

window.mainloop()
