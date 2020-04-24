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

def insert_sort():
    A 




