def is_simple_number(x):
    """определяет является ли число простым
    x - целое положительное число
    если простое True, иначе False"""
    divisor = 2
    while divisor < x:
        #esli x delitsya na delitel
        if x%divisor == 0:
            #chislo sostavnoe
            return False
        divisor += 1
    #chislo prostoe
    return True