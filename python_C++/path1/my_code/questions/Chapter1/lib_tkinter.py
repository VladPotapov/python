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
    window.geometry("600x600")
    if chk_state.get():
        js = "js"
    else:
        js = ""
    
    if chk_state2.get():
        python = "python"
    else:
        python = ""

    if chk_state3.get():
        cpp = "c++"
    else:
        cpp = ""

    if selected.get() == 1:
        lang = "js"
    elif selected.get() == 2:
        lang = "pyton"
    elif selected.get() == 3:
        lang = "c++"
    else:
        lang = ""

    hello.configure(text = "Имя: {}".format(txt.get()) + "\nУровень {}".format(combo.get()) + "\nЯ знаю " + js + " " + python + " " + cpp + "\nСамый крутой язык " + lang + "\nОбо мне: void AppearText(int x, int y, const char* text, COLORREF from, COLORREF to, int time, int steps)" + about.INSERT)
    

window = Tk()
#заголовок
window.title("Добро пожаловать в приложение Python")
#размер окна
window.geometry('600x350')

#текст в окне
lbl = Label(window, text="Привет", font=("Arial Bold", 50))
#расположение элемента
lbl.grid(column = 0, row = 0)

#ввод текста (Name)
txt = Entry(window, width = 25)
txt.grid(column = 1, row = 0)
#фокус ввода
txt.focus()

ans = Label(window, text = "Уровень")
ans.grid(column = 0, row = 3)


#выподающий список
combo = Combobox(window)
#значения
combo['values'] = ("начальный", "джуниор", "мидел", "сениор")
#значение по умолчанию
combo.current(0)
combo.grid(column = 1, row = 3)

clr = Label(window, text = "что вы знаете?")
clr.grid(column = 0, row = 4)

#checkbox
chk_state = BooleanVar()
#vibor po umolchaniyu
chk_state.set(True)
chk1 = Checkbutton(window, text= 'js', var = chk_state)
chk1.grid(column = 0, row = 5)

chk_state2 = BooleanVar()
chk2 = Checkbutton(window, text = 'python', var = chk_state2)
chk2.grid(column = 1, row = 5)

chk_state3 = BooleanVar()
chk3 = Checkbutton(window, text = "cpp", var = chk_state3)
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
about.insert(INSERT, 'Впишите сюда что-нибудь')
about.grid(column = 0, row = 9)

hello = Label(window, text = "")
hello.grid(column = 0, row = 10)

btn = Button(window, text = "click me", command = clicked)
btn.grid(column = 0, row = 11)

window.mainloop()
