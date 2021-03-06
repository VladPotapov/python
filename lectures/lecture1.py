#лекция 1
#программирование это
#   синтаксис языка
#   алгоритмы и структуры данных (важней синтаксиса и библиотек)
#   -----------------------------
#   прикладные библиотеки
#   практика
#   дизайн ПО
#   групповая работа

#синтаксис python   #имя    значение
x = 'hello world'   #x  --> hello world
#узнать тип         # \
print(type(x))      #  \
x = 1+2+3*2         #   9

#алгоритм
#primer 1
#обмен значения через 1 доп. переменную
a = 2
b = 5
tmp = a
a = b
b = tmp
print(a,b)
print()

#обмен через 2 доп. переменные
tmp1 = b
tmp2 = a
#или можно записать
#tmp1, tmp2 = b, a
a = tmp1
b = tmp2
#или можно записать
#a, b = tmp1, tmp2
print(a,b)
print()

#каскадное присвоение
x=y=z=0
print(x,y,z)
print()

#множественное присвоение
x, y, z = 1, 2, 3
print(x,y,z)
print()

#обмен без дополнительных переменных
a,b = b,a
print(a,b)
print()

#Арифмиетические операции

#возведение в степень
x = 2**3    #8
print(x)
print()

#корень числа
y = 3**0.5
print(y)
print()

# в степени в в степени с
a = 3
b = 2
c = 4
d = a**b**c #выполняется с права на лево
print(d)
print()

#умножение деление
#умножение
x = 2*3
#деление
x = 2
y = 3
z1 = x/y
z2 = x//y   #с отбрасыванием остатка
z3 = x%y    #возвращает остаток
print(type(z1)) #float
print(type(z2)) #int
print(type(z3)) #int
print()

#пометка
#a/b*c (разделить и результат умножить на c)
# 1,2

#теория групп
#группа по модулю числа
x = 3
y = 5
z = 5
#(x+y)%10
#----------------------->
# ' ' ' ' '  ' ' ' ' ' ' 
# 0 1 2 3 4  5 6 7 8 9 10
#  входит     не входит
#----------||------------

# ^__________|
print((x+y)%z)  #3
print()

#пример с отрицательным числом
x = (-11)//10
y = (-11)%10
print(x, y)
print()

#цикл while
#while условие: > #заголовок
    #оператор 1 '
    #оператор 2 '  тело
    #....       '   
#else  (не обязательно)
    #после всех итераций
#итерация - это однократное выполнение цикла (ход выполнения)
x = 3

while x > 0:
    y = x
    while y > 0:
        y -= 1
        print(y)
    x -= 1
print('stop')

#for является списочным
for x in 1,2,3,4,5:
    print(x**2)
#тоже самое
for x in range(1,6,1):
    print(x**2)
#в обратном порядке
for x in range(5,0,-1):
    print(x**2)
input('\nEnter')