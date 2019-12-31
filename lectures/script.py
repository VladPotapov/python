X = 5
Y = 2
Z = 2

def gcd(a, b):
    #функция подходящая для констант
    if a == b:
        return a
    elif a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)

num = gcd(X, Y)

print(num)