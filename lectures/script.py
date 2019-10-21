def arr(A,B):
    B = [0 if x<0 else x**2 for x in A if x % 2 == 0]
    return B
a1 = [1, 2, 3, 5, 7, 9, 18, 4]
b1 = []
itog = arr(a1, b1)

print(itog)