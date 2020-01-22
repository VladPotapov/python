def arr(Nmax):
    A = [0] * Nmax
    n = 0
    x = int(input())
    A[n] = x
    n += 1
    print(A)
    n -= 1
    x = A[n]
    print(A)

def arr1():
    A = []
    x = int(input())
    A.append(x)
    n = len(A)

def del_arr1(A):
    x = A.pop()

#list comprehension
A = [x**2 for x in range(10)]
# расшифровывается как
A = []
for x in range(10):
    A.append(x**2)

def  arr3():
    A = [1, 2, 3, 4, 5, 7, 12, 9, 6]
    B = []

    for x in A:
        if x % 2 == 0:
            B.append(x**2)

#тоже самое что и arr()
def arr4(A, B):
    B = [x**2 for x in A if x%2==0]
    return B

def arr5(A, B):
    B = [(0 if x < 0 else x**2) for x in A if x % 2 == 0]
    return B

#Квадратичные сортировки O(N**2) 
# сортировка вставками (insert sort) 
# постоянно меняет ячейки массива 
# 1 + 2 + 3 + 4 = N * (N - 1) / 2

# сортировка методом выбора (choise sort) 
# меняет ячеки по очерди не заглядывая в предыдущие 
# тот же алгоритм

# метод пузырька (bubble sort) 
# цель метода передвинуть самый большой элемент в конец 
# 4 + 3 + 2 + 1 = 10 (1+2... + (N -1) = N * (N - 1) / 2) 
# (N * (N - 1) / 2) * k

def insert_sort(A):
    """сортировка списка А вставками"""
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k],  A[k-1] = A[k-1], A[k]
            k -= 1

def choise_sort(A):
    """сортировка списка А выбором"""
    N = len(A)
    for  pos in range(0, N-1):
        for k in range(pos+1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]

def bubble_sort(A):
    """сортировка списка А методом пузырька"""
    N = len(A)
    for bypass in range(1, N):
        for k in range(0, N-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]

def test_sort(sort_algorithm):
    print("Тестируем. ", sort_algorithm.__doc__)
    print("testcase #1: ", end="")
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    print("ok" if A == A_sorted else "Fail")

    print("testcase #2: ", end="")
    A = list(range(10, 20)) + list(range(0, 10))
    A_sorted = list(range(20))
    sort_algorithm(A)
    print("ok" if A == A_sorted else "Fail")

    print("testcase #3: ", end="")
    A = [4, 2, 4, 2, 1]
    A_sorted = [1, 2, 2, 4, 4]
    sort_algorithm(A)
    print("ok" if A == A_sorted else "Fail")

#сортировка подсчётом (connt sort) 
# O(N) = требует O от N времени 
# O(M)  по памяти 
# где M количество элементов

if __name__ == "__main__":
    test_sort(insert_sort)
    test_sort(choise_sort)
    test_sort(bubble_sort)