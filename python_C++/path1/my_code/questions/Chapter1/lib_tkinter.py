#import tkinter = error
from tkinter import *

#виджет combobox выпадающий список
from tkinter.ttk import Combobox
#checkbox
from tkinter.ttk import Checkbutton

def clicked():
    #изменение заголовка
    lbl.configure(text="Вы выбрали")
    #принять значение из поля ввода
    res = "Привет {}".format(txt.get())
    hello.configure(text = res)
    #принять значение из списка
    combo_value = "Выбрано {}".format(combo.get())
    ans.configure(text = combo_value)
    

window = Tk()
#заголовок
window.title("Добро пожаловать в приложение Python")
#размер окна
window.geometry('600x250')

#текст в окне
lbl = Label(window, text="Привет", font=("Arial Bold", 50))
#расположение элемента
lbl.grid(column = 0, row = 0)

#ввод текста
txt = Entry(window, width = 25)
txt.grid(column = 1, row = 0)
#фокус ввода
txt.focus()

hello = Label(window, text = "Hello")
hello.grid(column = 0, row = 10)


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

window.mainloop()
