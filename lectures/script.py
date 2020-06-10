import random


def insert_sort(A):
    """Сортировка вставками"""
    pass


def choise_sort(A):
    """Сортировка выбором"""
    pass


def bubble_sort(A):
    """Сортировка пузырьком"""
    pass


def test_sort(sort_algorithm):
    # указывает каким методом сортируется список
    print("Тестируем: ", sort_algorithm.__doc__)

    print("testcase: #1 ", end="")
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    # встроенный тернарный оператор
    print("Ok" if A == A_sorted else "Fall")
    """
    тоже самое
    if A == A_sorted:
        print("Ok")
    else:
        print("Fall")
    """

    print("testcase: #2 ", end="")
    # арефметическая прогрессия
    A = list(range(10, 20)) + list(range(0, 5))
    A_sorted = list(range(20))
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fall")

    print("testcase: #3 ", end="")
    A = [4, 2, 4, 2, 1]
    A_sorted = [1, 2, 2, 4, 4]
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fall")


test_sort(insert_sort)
test_sort(choise_sort)
test_sort(bubble_sort)
