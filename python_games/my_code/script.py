import random

NUM_DIGITS = 3
MAX_GUESS = 10

def getSecretNum():
    numbers = list(range(10))
    random.shuffle(numbers)
    print(numbers)

getSecretNum()