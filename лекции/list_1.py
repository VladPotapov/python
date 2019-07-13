#primer 1

#узнать тип данных в python
x = 2
print(type(x))

#обмен значениями
#algoritm 1 (с помощью 1 дополнительной переменных)

#пример 1
a = 2
b = 5
tmp = a
a = b
b = tmp

#пример 2 (с помощью 2 дополнительны переменных)
a = 2
b = 5
tmp1 = b
tmp2 = a
#так же можно сделать
#tmp1, tmp2 = b, a
a = tmp1
b = tmp2

#пример 3
#тоже самое что и пример 2
a = 'hello'
b = 'world'
a,b = b,a

#world hello
print(a, b)

#каскадное присвоение
a=b=c=0

#множественное присваивание
x, y, z  = 1, 2, 3

#цикл while
def fun_while():
    x = 3
    while x>0:
        y = x
        while y > 0:
            y -= 1
            #выведет 2,1,0,1,0,0
            #если поменять местами y -= 1 и print(y)
            #будет 3,2,1,2,1,1
            print(y)
        x -= 1
    print('stop')

#цикл for
x = 2
for x in 1,2,3,4,5:
    #1,4,9,16,25
    print(x**2)

for x in range(1,6,1):
    #тоже самое
    print(x**2)

#Арифметические операции
#возведение в степень
x = 3
y = 2
z = x**y
print(z)

print()
#корень числа
x = 3
y = x**0.5
print(y)

print()
#a v stepeni b v stepeni c
a = 3
b = 2
c = 5
d = a**b**c
print(d)

#delenie
d1 = 5/7
#s otbrasivaniem ostatka
d2 = 5//7
#ostatok 
d3 = 5%7
print('/',d1, '//', d2, '%', d3)

#gruppa po modulyu chisla
x = 2
y = 7
#-------------------------->
# ' ' ' ' ' ' ' ' ' '
# 0 1 2 3 4 5 6 7 ne vhodit
# vhodit        z
#--------------''-----------
z = 7
#otvet 2
print((x+y)%z)
input('\nEnter')