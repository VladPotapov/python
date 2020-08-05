A = [3, 5, 7, 9]


def check_sorted(A, asending=True):
    """проверка отсортированности до O(len(A))"""
    flag = True
    s = 2 * int(asending) - 1

    for i in range(0, len(A) - 1):
        if s * A[i] > s * A[i + 1]:
            flag = False
            break
    print(flag)
    return flag


check_sorted(A)
