SYMBOLS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
MAX_KEY_SIZE = len(SYMBOLS)


def getMode():
    while True:
        print("зашифровать или расшифровать текст? ")
        mode = input().lower()

        if mode in ['зашифровать', 'з', 'расшифровать', 'р']:
            return mode
