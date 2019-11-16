num = "12352760992863415237661352".split()
for i in num:
    print(i, end=" ")
    
N = len(num)
F = [0] * 10

for i in range(N):
    x = int(input("Number "))
    F[x] += 1

for i in range(len(F)):
    print(F[i], end=" ")

print(l)