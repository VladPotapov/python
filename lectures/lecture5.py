#Массивы (тип list) 
#           
#     ---------
# A ->|1|2|3|4| - object list
#     ---|-----  
#        | 
#       тип

A = [1,2,3,4,5]

for x in A:
    print(x, type(x))  #тип элемента
    x += 1
    print(x)

print(type(A))  #тип list
print(A)

for k in range(5):  # = range(0,5,1)
    A[k] = A[k] * A[k]


# создать 1000 ячеек
B = [0] * 1000
top = 0

#       |  5   |
#       |  4   |
#       |  3   | --> 1000
#       |  2   |
#top    |  1   |
#       --------

def arr_b():
    x = int(input('Введите число '))
    top = 0
    while x != 0:
        B[top] = x
        top += 1
        x = int(input("число "))
    for k in range(4,-1,-1):
        print(B[k])

def copy_a():
    N = int(input('Number '))
    A = [0] * N
    B = [0] * N
    
    for k in range(N):
        A[k] = int(input('Number '))

    for k in range(N):
        B[k] = A[k] #поэлементное копирование

    C = A   #C ссылка на A

C = list(A) #C = A[:]

def array_search(A:list, N:int, x:int):
    """Осуществляет поиск числа х в массиве А
       от  до N-1 индекса включительно.
       Возвращает индекс элемента
       Или -1, если элемента нет
       Если в массиве одинаковые элементы
       Вернуть первый
    """
    for k in range(N):
        if A[k] == x:
            return k
    #если указать pass вместо return -1
    # функция будет возвращать None
    return -1

def test_array_searh():
    A1 = [1, 2, 3, 4, 5]
    m = array_search(A1, 5, 8)
    if m == -1:
        print("#test1 - ok")
    else:
        print("#test1 - fail")

    A2 = [-1, -2, -3, -4, -5]
    m = array_search(A2, 5, -3)
    if m == 2:
        print("#test2 - ok")
    else:
        print("#test2 - fail")

    A3 = [10, 20, 30, 40, 10]
    m = array_search(A3, 5, 10)
    if m == 0:
        print("#test3 - ok")
    else:
        print("#test3 - fail")

test_array_searh()

def invert_array1(A:list, N:int):
    """обращение массива (задом наперёд)
    в рамках индексов от 0 до N-1
    """
    #затерёт первые значения 
    # поменяв их последними
    for k in range(N):
        A[k] = A[N-1-k]

def invert_array2(A:list, N:int):
    #развернёт массив 2 раза 
    # вернув массив в изначальное состояние
    for k in range(N):
        A[k], A[N-1-k] = A[N-1-k], A[k]

def invert_array(A:list, N:int):
    """
    Обращение массива (поворот задом-наперёд)
    в рамках индексов от 0 до N-1
    """
    #делим N на 2 без остатка 
    # чтоб остановить обмен значениями на середине 
    # иначе массив не развернётся
    for k in range(N//2):
        #обмен значениями крест на крест
        A[k], A[N-1-k] = A[N-1-k], A[k]


def test_invert_array():
    A1 = [1, 2, 3, 4, 5]
    print(A1)
    invert_array(A1, 5)
    print(A1)
    if A1 == [5, 4, 3, 2, 1]:
        print('test1 ok')
    else:
        print('test1 fail')

    A2 = [0, 0, 0, 0, 0, 0, 0, 10]
    print(A2)
    invert_array(A2, 8)
    print(A2)
    if A2 == [10, 0, 0, 0, 0, 0, 0, 0]:
        print('test2 ok')
    else:
        print('test2 fail')

test_invert_array()

#Цикличиский сдвиг 
# бывает в лево и в право
# в лево двигает элемент вправо 
# в право двигает влево

#left 
# _______>
#|0|1|2|3|4|5| 
# |_________^
# tpm = 0

tmp = A[0]

def fun_left(a:list):
    N = len(a)
    for k in range(N-1):
        A[k] = A[k+1]
    A[N-1] = tmp




#right
#     <_______
#|0|1|2|3|4|5| 
# |_________|
#           tpm = 5

A = [0, 1, 2, 3, 4]

def fun_left(A:list):
    tmp = A[0]
    N = len(A)
    for k in range(N-1):
        A[k] = A[k + 1]
    A[N - 1] = tmp
    print(A)

def fun_right(A:list):
    N = len(A)
    tmp = A[N - 1]
    for k in range(N-2, -1, -1):
        A[k + 1] = A[k]
    A[0] = tmp
    print(A)

#решето эратосфена

arr = []
def arr_bool(A, N):
    A = [True] * N
    A[0] = A[1] = False
    for k in range(2, N):
        if A[k]:
            for m in range(2*k, N, k):
                A[m] = False
    for k in range(N):
        print(k, ' - ', 'простое' if A[k] else 'состовное')
                        #---------------------------------
                        #тернарный оператор

arr_bool(arr, 5)
