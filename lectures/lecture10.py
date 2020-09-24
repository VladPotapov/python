# Реализация Бинарного поиска в массиве 
# требование: 
#   массив отсортирован по возрастанию 
#   left_boundary = левая граница на 1 меньше искомого елемента 
#   right_boundary = правая на 1 больше искомого элемента 
#   right = указывает на искомое между left_boundary, right_boundary
# А = [1, 2, 3, 6, 7, 9] 
# если x = 5 то left_boundary = 3, right_boundary = 6 
# если x = 15 то left_boundary = 9, 
# right_boundary = выходит за границы массива

# поиск для левой части массива
# принимает массив и ключ
def left_bound(A, key):
    # крайняя позизиция 
    # поиск не будет осуществляться 
    # если искомое меньше минимального числа в массиве
    left = -1
    # если искомое число 
    # равно максимальному числу в массиве 
    # будет только крайняя левая
    right = len(A)

    while right - left > 1:
        # делим массив по полам 
        # отбрасывая лишнюю часть
        middle = (left + right) // 2

        # отыскиваем крайнюю левую 
        # и правую часть искомого числа
        if A[middle] < key:
            left = middle
            print(A[left])
        else:
            right = middle
            print(A[right])

    return left

# принимает массив и ключ
def right_bound(A, key):
    left = -1
    right = len(A)

    while right - left > 1:
        middle = (left + right) // 2

        if A[middle] <= key:
            left = middle
        else:
            right = middle

    return right


# Динамическое программирование
# число фибоначи 
# Fn = (Fn - 1) + (Fn - 2) 
# O(Fibn) 

# выполняется очень медленно 
# использовать не рекомендуется
def fib(n):
    if n <= 1:
        return 1
    
    return (fib(n - 1) + fib(n - 2))

#   n | 0 | 1 | 2 | 3 | 4 |...
# fib | ? | ? | ? | ? | ? |...

# не экономно
def fib2():
    n = int(input())
    fib = [0, 1] + [0] * (n - 1)

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

# кузнечик 
# 0_1_2_3_4_5____N - 2_N - 1_N
# | | | | | | 
# сколько различный траекторий у кузеничика из 1 до N 
# возможность попасть в N можно 2 способами из N-1, N-2 
# Kn = Kn2 + Kn1

def trag_num(N):
    # создание массиво соответствующее количествам в K
    K = [0, 1] + [0] * (N - 1)

    for i in range(2, N - 1):
        K[i] = K[i - 2] + K[i - 1]

    print(len(K))
    return K[N]


# запретить некоторые клетки

def count_tragectories(N, allowed:list):
    K = [0, 1, int(allowed[2])] + [0] * (N-3)

    for i in range(3, N + 1):
        if allowed[i]:
           K[i]  = K[i - 1] + K[i - 2] + K[i - 3]
           print(K[i])


# минимальная стоимость достижения клетки N
# price[i] - за посещение клетки i 
# C[i] - cost минимальная стоимость достижения кклетки i
# 0____,____i 
# i-2  i-1 
# Ci = price + min(Ci - 2, Ci - 1)
# Exemple: 
# С1 = price1 
# C2 = price1 + price2
