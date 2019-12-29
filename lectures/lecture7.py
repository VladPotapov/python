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

window = gr.GraphWin("Russian game", 600, 600)
alpha = 0.1

def fractal_rectangle(A, B, C, D, deep = 10):
    if deep < 1:
        return
    
    #*A = A[0], A[1] и т.д.
    #gr.Line(gr.Point(*A), gr.Point(*B))

    for M, N in (A, B), (B, C), (C, D), (D, A):
        gr.Line(gr.Point(*M), gr.Point(*N)).draw(window)
    
    A1 = (A[0] * (1-alpha) + B[0] * alpha, A[1] * (1-alpha) + B[1] * alpha)
    B1 = (B[0] * (1-alpha) + C[0] * alpha, B[1] * (1-alpha) + C[1] * alpha)
    C1 = (C[0] * (1-alpha) + D[0] * alpha, C[1] * (1-alpha) + D[1] * alpha)
    D1 = (D[0] * (1-alpha) + A[0] * alpha, D[1] * (1-alpha) + A[1] * alpha)

    fractal_rectangle(A1, B1, C1, D1, deep-1)

fractal_rectangle((100, 100), (500, 100), (500, 500), (100, 500), 100)

#Факториал 
# n!= (n-1)!*n 
# f(n) {
# 1 || n <= 1 
# f(n) * n, n > 1
# }


input("\nEnter")