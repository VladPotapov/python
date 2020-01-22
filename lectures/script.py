def  arr3():
    A = [1, 2, 3, 4, 5, 7, 12, 9, 6]
    B = []

    for x in A:
        if x % 2 == 0:
            B.append(x**2)
    
    print(B)
    
arr3()