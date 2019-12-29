from tkinter import *

text = "proverka"

def click():
    res = "{}".format(text)
    txt.configure(text = res)

window = Tk()
window.geometry('300x300')

ans = Entry(window, width = 25)
ans.grid(column = 0, row = 0)
ans.focus()

btn = Button(window, text="proverka", command = click)
btn.grid(column = 0, row = 1)

txt = Label(window, text="")
txt.grid(column = 1, row = 0)

window.mainloop()