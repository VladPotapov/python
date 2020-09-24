# -*- coding: utf-8 -*-
# Шифр Цезаря 
# version 2.0

SYMBOLS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя 0123456789!@#$%^&*().,'
MAX_KEY_SIZE = len(SYMBOLS)

# функция для определения шифровки или расшифровки


def getMode():
    while True:
        print("зашифровать, расшифровать или взломать текст? ")
        mode = input().lower()

        if mode in ['зашифровать', 'з', 'расшифровать', 'р', 'взломать', 'в']:
            return mode
        else:
            print('Введите "зашифровать" или "з" чтоб зашифровать')
            print('Введите "расшифровать" или "р" чтоб расшифровать')
            print('Для взлома введите "взломать" или "в"')

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

            if symbolIndex >= len(SYMBOLS):
                symbolIndex -= len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)
            
            translated += SYMBOLS[symbolIndex]

    return translated

mode = getMode()
message = getMessage()
mode = getMode()
message = getMessage()
if mode[0] != 'в':
    key = getKey()

print("Преобразованный текст: ")
if mode[0] != 'в':
    print(getTranslatedMessage(mode, message, key))
else:
    for key in range(1, MAX_KEY_SIZE + 1):
        print(key, getTranslatedMessage('расшифровать', message, key))
