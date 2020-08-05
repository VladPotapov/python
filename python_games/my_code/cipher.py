SYMBOLS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
MAX_KEY_SIZE = len(SYMBOLS)

# функция для определения шифровки или расшифровки


def getMode():
    while True:
        print("зашифровать или расшифровать текст? ")
        mode = input().lower()

        if mode in ['зашифровать', 'з', 'расшифровать', 'р']:
            return mode
        else:
            print('Введите "зашифровать" или "з" чтоб зашифровать')
            print('Введите "расшифровать" или "р" чтоб расшифровать')

# принимает текст для обработки


def getMessage():
    print("Введите текст: ")
    return input()

# принимает ключ


def getKey():
    key = 0

    while True:
        print("Введите ключ шифрования (1-%s)" % (MAX_KEY_SIZE))
        key = int(input())

        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'p':
        key = -key
    translated = ''

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)

        # Символ не найден в SYMBOLS.
        if symbolIndex == -1:
            translated += symbol
        else:
            # зашифровать или расшифровать
            symbolIndex += key
