import random
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O]  |
 /|\  |
 / \  |
     ===''']

words = {
   'Цвета':'красный ораньжевый жёлтый зелёный синий голубой фиолетовый белый чёрный коричневый серый розовый бежевый'.split(),
   'Фигуры':'квадрат прямоуголник многоугольник триугольник ромб овал круг окружность эллипс трапеция параллелограмм'.split(),
   'Фрукты':'яблоко апельсин мандарин банан персик арбуз груша слива лимон лайм грейфрукт абрикос виноград киви манго нектарин'.split(),
   'Животные':'аист акула бабуин баран барсук бобр бык верблюд волк воробей ворон выдра голубь гусь жаба зебра змея индюк кит кобра коза козел койот корова кошка кролик крыса курица лама ласка лебедь лев лиса лосось лось лягушка медведь моллюск моль мул муравей мышь норка носорог обезьяна овца окунь олень орёл осёл панда паук питон попугай пума семга скунс собака сова тигр тритон тюлень утка форель хорёк черепаха ястреб ящерица'.split()
}

abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def getRandomWord(wordDict):
   """функция возвращает случайную строку из списка"""
   # выбор случайного ключа
   wordKey = random.choice(list(wordDict.keys()))
   # выбор случайного слова
   wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
   return [wordDict[wordKey][wordIndex], wordKey]
   

def displayBoard(missedLetters, correctLetters, secretWord):
   print(HANGMAN_PICS[len(missedLetters)])
   print()

   print('Ошибочные буквы: ', end=' ')
   for letter in missedLetters:
      print(letter, end=' ')
   print()

   blanks = '_' * len(secretWord)

   for i in range(len(secretWord)):
      if secretWord[i] in correctLetters:
         blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
   
   for letter in blanks:
      print(letter, end=' ')
   
   print()

def getGuess(alreadyGuessed):
   """возвращает букву, введеную игроком. Эта функция проверят, что игрок ввёл только одну букву и ничего больше"""
   while True:
      print('Введите букву.')
      guess = input('введите букву ')
      guess = guess.lower()
      if len(guess) != 1:
         print('введите одну букву ')
      elif guess in alreadyGuessed:
         print('Вы уже называли эту букву')
      elif guess not in abc:
         print("введите букву")
      else:
         return guess
      
def playAgain():
   """возвращае True если игрок хочет ещё раз сыграть"""
   print('Хотите сыграть ещё раз? (да или нет)')
   return input().lower().startswith('д')

print('В И С С Е Л И Ц А')

#если выбрать пустую строку 
# цикл while будет пропускаться
difficulty = '.'

while difficulty not in 'ЛСТ':
   print('Выберите уровень сложности Л - лёгкий, С - средний, Т - тяжёлый')

   difficulty = input().upper()

if difficulty == 'С':
   del HANGMAN_PICS[8]
   del HANGMAN_PICS[7]

if difficulty == 'T':
   del HANGMAN_PICS[8]
   del HANGMAN_PICS[7]
   del HANGMAN_PICS[5]
   del HANGMAN_PICS[3]

missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False

while True:
   print('Секретное слово из набора: ' + secretSet)
   displayBoard(missedLetters, correctLetters, secretWord)

   #Позволяет игроку ввести букву
   guess = getGuess(missedLetters + correctLetters)

   if guess in secretWord:
      correctLetters = correctLetters + guess

      #Проверяет выйграл ли игрок
      foundAllLetters = True
      for i in range(len(secretWord)):
         if secretWord[i] not in correctLetters:
            foundAllLetters = False
            break
      if foundAllLetters:
         print('Да! секретное слово - "' + secretWord + '" Вы угадали')
         gameIsDone = True
   else:
      missedLetters = missedLetters + guess

      #Проверяет, превысил ли игрок лимит попыток и проиграл
      if len(missedLetters) == len(HANGMAN_PICS) - 1:
         displayBoard(missedLetters, correctLetters, secretWord)
         print('Вы ичерпали все попытки!\n Не угадано букв: ' + str(len(missedLetters)) + ' и угадано букв: '  + str(len(correctLetters)) + ' было загадно слово "' + secretWord + '"')
         gameIsDone = True

   #Спрашиваем, хочет ли игрок сыгарать заново
   if gameIsDone:
      if playAgain():
         missedLetters = ''
         correctLetters = ''
         gameIsDone = False
         secretWord, secretSet = getRandomWord(words)
      else:
         break