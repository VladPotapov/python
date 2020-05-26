import random

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