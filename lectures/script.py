X = 225
Y = 800

def gcd(a, b):
    #функция подходящая для констант
    if a == b:
        return a
    elif a > b:
        #a - b остаток от вычитания a на b 
        # если при вычитании а 
        # становиться меньше b 
        # из b вычитается a 
        # до тех пор пока не останется 0
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)

num = gcd(X, Y)

print(num)