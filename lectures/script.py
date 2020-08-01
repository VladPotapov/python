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


arr = [2, 7, 5, 3, 9]

hoar_sort(arr)
