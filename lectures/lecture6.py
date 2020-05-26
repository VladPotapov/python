# -*- coding: utf-8 -*-
import random

# у массива с фиксированным размером 
# надо вручную отслеживать уровень заполнения 
def level_array():
    N_max = 10
    A = [0] * N_max
    # n одновременно является индексом 
    # и количеством элементов
    n = 0
    x = int(input("Number "))
    #кладу x в ячейку под номером n
    A[n] = x
    #после увеличиваю n
    n += 1
    print(A)

#level_array()

#level_array2 делает тоже что и функция level_array
def level_array2():
    A = []
    x = int(input("Number "))
    A.append(x)
    n = len(A)
    print(A)
    print(n)

#level_array2()

#удаление с конца
def delete_element():
    A = [1, 2, 3, 4, 5, 7]
    n = len(A)
    x = A[n - 1]
    A = A[0:n - 1]
    print(A)
    print(n)
    print(x)

#delete_element()

def delete_element2():
    A = [1, 2, 3, 4, 5, 7]
    n = len(A)
    x = A.pop()
    print(A)
    print(n)
    print(x)

#delete_element2()

# List comprehensions

def list_compr():
    # variant a
    A = [x ** 2 for x in range(10)]
    B = []
    # or
    # variant b работает медленее 
    # чем варинт a
    for x in range(10):
        B.append(x ** 2)

    C = [x + 1 for x in range(10)]
    print(A)
    print(B)
    print(C)

#list_compr()

# Поиск чётных чисел

def even_number():
    A = [1, 2, 3, 4, 5, 7, 9, 12, 6]
    B = []
    for x in A:
        if x % 2 == 0:
           B.append(x ** 2) # или x * x

# even_number2 делает тоже что и even_number
def even_number2(A, B):
    # так
    B = [x ** 2 for x in A if x % 2 == 0]
    print(B)
    #  (0 if x < 0 else x ** 2) = x ** 2
    B = [(0 if x < 0 else x ** 2) for x in A if x % 2 == 0]
    print(B)


# сортировка 
# Квадратичные сортировки O(N**2)
# количество операций на обработку массива равно примерно N ** 2 
# где N длина массива 
# Асимптотика (работа с памятью) или (скорость вычисления) 
# сортировка требует больше операций остальных 
# чем другие (циклический сдвиг) 
# сортировка вставками (insert sort)

#метод вставками 
# (bubble sort)
# сортировка из 5 элементов 
# 1 + 2 + 3 + 4 = 10 
# ((N * (N - 1)) / 2) * k
A_insert = [4, 2, 5, 1, 3]
def insert_sort(nums):
    # Начнем со второго элемента, так как мы предполагаем, что первый элемент отсортирован
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        # И сохранить ссылку на индекс предыдущего элемента
        j = i - 1
        # Переместить все элементы отсортированного сегмента вперед, 
        # если они больше, чем элемент для вставки
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        # вставляем элемент
        nums[j + 1] = item_to_insert

# insert sort и choice sort 
# использует N - 1 проход 


# метод выбора
def choice_sort():
    A = [4, 2, 5, 1, 3]
    N = len(A)
    #индекс первой ячейки
    i = 0

    # последний элемент сортировать не надо
    while i < N - 1:
        # переменная m будет хранить минимальное значение 
        # изначально это i
        m = i
        # поиск ячейки следующей за i
        j = i + 1
        while j < N:
            # сравниваем значение ячеек
            if A[j] < A[m]:
                m = j
            j += 1
        # обмен значений
        # в ячейку i записывается минимум 
        # а значение из i записывается 
        # на старое место минимума
        A[i], A[m] = A[m], A[i]
        # переход к следующей ячейки
        i += 1
    print(A)

# сортировка методом пузырька 
# (bubble sort)
# сортировка из 5 элементов 
# 4 + 3 + 2 + 1 = 10
# 1 + 2 + ...(N - 1) = (N * (N - 1)) / 2
# пример: 
# (5 * (5 - 1)) / 2 = 10

def bubble_sort_for():
    # количество элементов
    N = 10
    a = []

    for i in range(N):
        a.append(random.randint(1, 99))
    print(a)

    for i in range(N - 1):
        for j in range(N - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    print(a)

def bubble_sort_while():
    N = 10
    a = []
    for i in range(N):
        a.append(random.randint(1, 100))
    print(a)

    i = 0
    while i < N - 1:
        j = 0
        while j < N - 1 - i:
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
            j += 1
        i += 1
    print(a)