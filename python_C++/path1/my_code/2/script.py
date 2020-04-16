# -*- coding: utf-8 -*-

name = "Roma"
age = 35
rost = 1.45
boo = True

print(type(name))
print(type(age))
print(type(rost))
print(type(boo))

print(123 + 456)

#тоже самое
num1 = 123
num2 = 456
print(num1 + num2)

#ввести 2 числа 
num1 = int(input("Первое число "))
num2 = int(input("Второе число "))
# найти их сумму
summa = num1 + num2 
# вывести результат
print(summa)

print("Другой способ 2")
print()
s = input()
num1, num2 = s.split()
num1 = int(num1)
num2 = int(num2)
print(num1, "+", num2, "=", num1 + num2)

#тоже самое
print("способ 3")
n1, n2 = input().split()
n1 = int(n1)
n2 = int(n2)
print(n1,"+", n2, "=", n1+n2)

print("способ 4")
n1, n2 = map(int, input("Number: ").split())
print(n1 + n2)
input("\nEnter")
