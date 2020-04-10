# -*- coding: utf-8

print("как тебя зовут? ", end="")
name = input()
print("Привет ", name, "!", sep="")

name = "Платон"
name = "Сократ"
name = input("Как тебя зовут? ")
print("Привет", name, "!")

for i in range(len(name)):
    print(i, "=", name[i])

print("Наоборот")

N = len(name)
for i in range(N):
    print(name[N - 1])
    N -= 1

input("\nEnter")