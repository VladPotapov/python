def positive_sum (arr):
    summa = 0
    for i in range(len(arr)):
        if arr[i] >= 0:
            summa += arr[i]

    if arr == []:
        return 0

    return summa


my_arr1 = [-1, 2, -5, 7, 9]
my_arr2 = []
my_arr3 = [-3, -5, -7, -1]

print(positive_sum(my_arr3))