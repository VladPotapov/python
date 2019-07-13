#вариант 1
print('введите пример(например 2 + 2): ')
s = '2 + 2'
num1, op, num2 = s.split()
print(num1)
print(op)
print(num2)

#вариант 2
print('введите два числа ')
#str
n1, n2 = '5 7'.split()
#int
n1, n2 = int(n1), int(n2)
if n1 > n2:
    print('n1 bolshe')
elif n1 < n2:
    print('n2 bolse')
else:
    print('n1 == n2')

print('numbers x and y')
#preobrazuet str in int
x, y = map(int, input().split())
print(type(x))

#dopustimie peremennie
m11 = 11
Vasya = 'name'
CY_27 = 'samalet'
_24 = 24

a = 4
b = 5
c = 9

print(c, '-', b, '=', a, sep="")
input('\nEnter')