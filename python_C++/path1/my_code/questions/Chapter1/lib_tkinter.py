#import tkinter = error
from tkinter import *

#виджет combobox выпадающий список
from tkinter.ttk import Combobox

def clicked():
    res = "Привет {}".format(txt.get())
    lbl.configure(text="Я же просил...")
    hello.configure(text = res)

def my_ans():
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

hello = Label(window, text = "")
hello.grid(column = 0, row = 2)

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

btn = Button(window, text="не нажимать", bg="black", fg="red", command=clicked)
btn.grid(column = 2, row = 0)

btn2 = Button(window, text="выбрать", width = 50, command = my_ans)
btn2.grid(column = 0, row = 4)

window.mainloop()
