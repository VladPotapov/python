from tkinter import *
import random
import module
#для вывода голоса
import pyttsx3

def click():
    """
    принимает ответ пользователя
    передаёт его в функцию main
    """
    res = "{}".format(inp.get()).lower()
    main(res)

def main(que):
    ans = milling(que)
    #вывод голосового сообщения
    engine = pyttsx3.init()
    engine.say(ans)
    engine.runAndWait()
    #вывод текста в окне
    txt.configure(text = ans)

def milling(que):
    if que in module.hello:
        length = len(module.ans_hello) - 1
        index = random.randint(0, length)
        return module.ans_hello[index]
    elif que in module.how_you:
        length = len(module.ans_how_you) - 1
        index = random.randint(0, length)
        return module.ans_how_you[index]
    elif que in module.bye:
        length = len(module.ans_bye) - 1
        index = random.randint(0, length)
        return module.ans_bye[index]
    elif que in module.programms:
        #запуск программ
        import os
        for i in range(len(module.programms)):
            if que == module.programms[i]:
                play = module.ans_programms[i]
                os.system(play)
    elif que in module.none_text:
        return "Вы ничего не ввели"
    else:
        return "чё чё чё?"

#окно приложения
window = Tk()
window.title("проект Миллиган")
window.geometry('400x400')

h1 = Label(window, text = "Миллиган", font = ("Arial Bold", 40))
h1.grid(column = 0, row = 0)

h2 = Label(window, text = "Пообщайся с Миллиганом и его 40 личностями", font = ("Arial Bold", 13))
h2.grid(column = 0, row = 1)

p = Label(window, text = "Задайте вопрос?", font = ("Arial Bold", 10))
p.grid(column = 0, row = 2)

inp = Entry(window, width = 30)
inp.grid(column = 0, row = 3)
inp.focus()

txt = Label(window, text = "", width = 44, font = ("Arial Bold", 12), bg = "black", fg = "red")
txt.grid(column = 0, row = 5)

btn = Button(window, text = "Спросить", command = click)
btn.grid(column = 0, row = 7)

window.mainloop()

input("\nEnter")