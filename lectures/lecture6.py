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

def arr3():
    B = []
    A = [1, 2, 3, 4, 5, 7, 9, 12, 6]
    for x in A:
        if x % 2 == 2:
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
# сортировка методом выбора (choise sort)