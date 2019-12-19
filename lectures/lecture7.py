import graphics as gr
# Рекурсия 
# репа = дед + баба + внучка + собака + кошка + мышка 
# 200    100    50      30       10       9       1 
# подзадача должна быть проще задачи 
# n = 5 --> n = 4 --> n = 3 --> n = 2 --> n = 1  
# ^---------|^--------|^--------|^--------| 
#плохой вариант рекурсии
# def f():
#   f() 
# 
# 1)рекуретный случай - способ обработки
# 2)крайний случай - решить каким он будет 
# если не решить 1 и 2 рекурсию не писать

def matryoshka(n):
    if n == 1:
        print("Матрёшечка")
    else:
        print("Верх матрёшки n = ", n)
        matryoshka(n-1)
        print("Низ матрёшки n = ", n)
         
#matryoshka(5)
#      a1
#   a--|-------b    aa1 = alfa * ab
#   |          |_b1
#   |          |
#   |          |
#d1-|          |
#   d-------|--c 
#           c1 
#глубина рекурсии

window = gr.GraphWin("Russian game", 300, 300)
alpha = 0.2

def fractal_rectangle(a, b, c, d, deep = 5):
    if deep < 1:
        return
    
    for M, N in (a, b), (c, d), (d, a):
        gr.Line(gr.Point(*M), gr.Point(*N)).draw(window)

        A1 = (A[0] * (1 - alpha) + B[0] * alpha, A[1] * (1 - alpha) + B[1] * alpha)
        B1 = (B[0] * (1 - alpha) + C[0] * alpha, B[1] * (1 - alpha) + C[1] * alpha)
        C1 = (C[0] * (1 - alpha) + D[0] * alpha, C[1] * (1 - alpha) + D[1] * alpha)
        D1 = (D[0] * (1 - alpha) + A[0] * alpha, D[1] * (1 - alpha) + A[1] * alpha)
        fractal_rectangle(A1, B1, C1, D1, deep-1)

#A1x = (1-alpha) * Ax + alpha * Bx 
# = A1 = (A[0] * (1 - alpha) + B[0] * alpha, A[1] * (1 - alpha) + B[1] * alpha)

fractal_rectangle((100, 100), (500, 100), (500, 500), (100, 500))
input("\nEnter")