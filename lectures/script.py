def delete_element():
    A = [1, 2, 3, 4, 5, 7]
    n = len(A)
    n -= 1
    x = A[n]
    print(A)
    print(x)
    print(n)

#delete_element()

def delete_element2():
    A = [1, 2, 3, 4, 5, 7]
    n = len(A)
    x = A.pop()
    print(A)
    print(n)
    print(x)

delete_element2()

