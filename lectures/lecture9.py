# Сортировка слиянием
# Слияние отсортированных массивов
# A = i, B = k, C = n
# Сортировка называется устойчивой
# если она не меняет порядок равных элементов
# (тоесть если если элементы из 2х массивов равны
# сначало будет добавлен элемент из первого массива)

def merge(A: list, B: list):
    C = [0]*(len(A)+len(B))
    i = k = n = 0

    while i < len(A) and k < len(B):
        # для устойчивой сортировки используется <=
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
            n += 1
        else:
            C[n] = B[k]
            k += 1
            n += 1

    while i < len(A):
        C[n] = A[i]
        i += 1
        n += 1

    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1

    return C

# Рекурсивная функция
# проверяем крайний случай


def merge_sort(A):
    if len(A) <= 1:
        return

    middle = len(A) // 2

    # левая половина
    L = [A[i] for i in range(0, middle)]
    R = [A[i] for i in range(middle, len(A))]

    merge_sort(L)
    merge_sort(R)

    C = merge(L, R)

    # если написать А = С
    # то ответ не сохранится
    # вместо этого лучше сделать
    for i in range(len(A)):
        A[i] = C[i]

# Сортировка Тони Хоара (Quick Sort)
# A [      ] основной массив
# barrier = A[0]
# L [] динамический массив для маллых значений
# M [] динамический массив для средних значений
# R [] динамический массив для больших значений


def hoar_sort(A):
    # крайний случай
    if len(A) <= 1:
        return

    barrier = A[0]

    L = []
    M = []
    R = []

    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)

    hoar_sort(L)
    hoar_sort(R)

    # счётчик
    k = 0

    # затратно по памяти
    for x in L+M+R:
        A[k] = x
        k += 1

    print(A)


def check_sorted(A, asending=True):
    """проверка отсортированности до O(len(A))"""
    flag = True
    s = 2 * int(asending) - 1

    for i in range(0, len(A) - 1):
        if s * A[i] > s * A[i + 1]:
            flag = False
            break
    return flag

    # Бинарный поиск в массиве
