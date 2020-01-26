from tkinter import *
from tkinter import messagebox


# информационное окно
def info():
    messagebox.showinfo('Заголовок', 'Текст')

# предупреждение
def warning():
    messagebox.showwarning("Предупреждение", "Будьте внимательны")

# error
def error():
    messagebox.showerror("Error", "Error 400")

def messages():
    # возвращает true, false
    res1 = messagebox.askquestion('Вопрос 1', 'Хотите продолжить?')
    # возвращает true, false
    res2 = messagebox.askyesno("Вопрос 2", "Ты точно хочешь продолжить?")
    # возвращает true, false, none
    res3 = messagebox.askyesnocancel("Вопрос 3", "Что так хочется потыкать?")
    # возвращает true, false
    res4 = messagebox.askokcancel("Вопрос 4", "Ну как нравиться тыкать?")
    # возвращает true, false
    res5 = messagebox.askretrycancel("Вопрос 5", "Ну что поехали дальше?")

    txt.config(text = "res1 = " + str(res1) + ", res2 = " + str(res2) + ", res3 = " + str(res3) + ", res4 = " + str(res4) + ", res5 = " + str(res5))

root = Tk()
root.title("Приложение Python")
root.geometry("500x500")

btn = Button(root, text = "click", command = info)
btn.grid(row = 0, column = 0)

btn1 = Button(root, text = "warning", command = warning)
btn1.grid(row = 0, column = 1)

btn2 = Button(root, text = "не нажимать", command = error)
btn2.grid(row = 0, column = 2)

btn3 = Button(root, text = "сообщения", command = messages)
btn3.grid(row = 1, column = 0)

txt = Label(root, text = "Text")
txt.grid(row = 2, column = 0)


root.mainloop()