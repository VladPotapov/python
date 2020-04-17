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
    N = len(A)
    x = int(input("Number "))
    N -= 1
    A[N] = x
    print(A)
    print(N)
    print(x)

delete_element()

def delete_element2():
    A = [1, 2, 3, 4, 5, 7]
    n = len(A)
    x = A.pop()
    print(A)
    print(n)
    print(x)

#delete_element2()

