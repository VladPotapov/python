#Генерация всех перестановок 
#{ 1, 2, 3,...N} -числа которые требуется переставлять
# Nx(N-1)x...*2*1 = N! 
# |___|__|____|
# Упрощаем - все числа 
# от ,0,0..,0, до ,N-1,..,N-1,

def gen_bin(M:int, prefix = ""):
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    
    for digit in "0", "1":
        gen_bin(M - 1, prefix + digit)

def generate_nambers(N:int, M:int, prefix = None):
    """
    Генерирует все числа (с лидирующими незначащими нулями)
    в N-ричной системе счисления (N <= 10)
    длины M
    """
    prefix = prefix or []

    if M == 0:
        print(prefix)
        return

    for digit in range(N):
        prefix.append(digit)
        generate_nambers(N, M - 1, prefix)
        prefix.pop()

#только для 2ой системы
#gen_bin(5)

#для любой
#generate_nambers(4, 3)

def find(number, A):
    """ищет number в А и возвращает True / False"""
    for x in A:
        if number == x:
            return True
    return False

#find2 == find
def find2(number, A):
    flag = False
    for x in A:
        if number == x:
            flag = True
            break
    return flag

def generate_permutations(N:int, M:int = -1, prefix = None):
    """
    Генерация всех перестановок N чисел в M позициях,
    с префиксах prefix
    """
    #если M = -1 то M = N иначе M
    M = N if M == -1 else M
    prefix = prefix or []

    if M == 0:
        #*prefix уберает скобки
        print(prefix)
        return
    
    for number in range(1, N + 1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permutations(N, M - 1, prefix)
        prefix.pop()

generate_permutations(3)

# Рекуррентные сортировки 
# Сортировка Тони Хоара (быстрая) 
# W(N*log**2 N) сортирует до O(N**2) 
# сортирующее действие выполняется на:
# прямом ходу 
# без дополнительной памяти 
# относится к алгоритмам 
# "разделяй и влавствуй" 
# [4, 2, 5, 3, 1] 
# барьерный элемент (случайный элемент из списка) 
# отправляет элемент меньше себя в лево а больший в право 
# сортируется по 3 элемента

# Сортировка слиянием 
# O(N*log**2 N) 
# сортирующее действие выполняется на: 
# обратном ходу 
# нужно O(N) дополнительной памяти 
# часть А от 0 до N//2 не включительно 
# часть В от N//2 вкл. до N не вкл. 
# после создаётся пустой массив 
# куда переносяться элементы по возрастанию 
# из 2 отсартированных частей с помощью сравнения 
# [3, 5, 1, 4, 2, 6] 
# [1, 3, 5 |2, 4, 6] 
# дальше сравниваються 2 части 
# и переносяться в новый массив 
# удаляясь из старого
# [1, 2, 3, 4, 5, 6]