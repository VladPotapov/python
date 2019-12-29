def factorial(n:int):
    #утверждение
    assert n >= 0, "факториал отр. не определён"

    if n == 0:
        return 1