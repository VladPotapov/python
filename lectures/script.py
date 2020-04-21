def even_number():
    A = [1, 2, 3, 4, 5, 7, 9, 12, 6]
    B = []
    for x in A:
        if x % 2 == 0:
           B.append(x ** 2) # или x * x
    print(B)

even_number()