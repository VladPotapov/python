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

def f(n:int):
    #утверждение
    assert n >= 0, "факториал отр. не определён"

    if n == 0:
        return 1
    
    #умножаем число на n = 1 
    # постепенно увеличивая n на 1
    return f(n - 1) * n

# Алгоритм Евклида 
# a |__|__|__|__|__|__| 
#            |________| - (a - b):d (делитель)
# b |__|__|__| 
# НОД (a, b) = НОД(a - b, b) 
# gcd(a, b) = {
# a, a = b 
# gcd(a - b, b), a > b 
# gcd(a, b - a), b > a
# }

X = 225
Y = 800

def gcd(a, b):
    #функция подходящая для констант
    #ищит общий делитель
    if a == b:
        return a
    elif a > b:
        #a - b остаток от вычитания a на b 
        # если при вычитании а 
        # становиться меньше b 
        # из b вычитается a 
        # до тех пор пока не останется 0
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)

num = gcd(X, Y)

#НОД (a, b) = НОД(a % b, b)

def gcd2(a, b):
    if b == 0:
        return a
    else:
        return gcd2(b, a % b)

def gcd3(a, b):
    return (a if b == 0 else gcd3(b, a % b))

#Быстрое возведение в степень
#a**n = a * a * a * a обочное возведение в степень n раз

#подходит при положительном числе
#a**n = a**n-1*a
#a**0 = 1 
# pow(a, n) {
# 1, n = 0 
# pow(a, n-1)*a, n > 0 (n - нечёт.)
# pow(a**2, n//2), n чёт
# }

def pow(a:float, n:int):
    if n == 0:
        return 1
    elif n%2 == 1:  #нечётное
        return pow(a, n-1) * a
    else:   #чётное
        return pow(a**2, n//2)

#a**2k = (a**2)k или  a**n = (a**2)**n/2
    

input("\nEnter")