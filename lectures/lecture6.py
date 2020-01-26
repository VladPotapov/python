def fun():
    N = 10
    # указываем максимальное число вложенностей
    A = [0] * N
    n = 0
    x = int(input("Number: "))
    A[n] = x
    n += 1
    print(A)

def fun1():
    # массив это объект (модифицированный список)
    A = []
    x = int(input("Number: "))
    # автомотическое добавление элементов
    A.append(x)
    n = len(A)
    print(n)

def fun2():
    A = [1, 2, 3, 4, 5, 7]
    n = len(A)
    # удаление с конца
    x = A.pop()
    print(A)




