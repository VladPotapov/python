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
     ===''']
words = 'аист акула бабуин баран барсук бобр бык верблюд волк воробей ворон выдра голубь гусь жаба зебра змея индюк кит кобра коза козел койот корова кошка кролик крыса курица лама ласка лебедь лев лиса лосось лось лягушка медведь моллюск моль мул муравей мышь норка носорог обезьяна овца окунь олень орёл осёл панда паук питон попугай пума семга скунс собака сова тигр тритон тюлень утка форель хорёк черепаха ястреб ящерица'.split()

def getRandomWord(wordList):
   wordIndex = random.randint(0, len(wordList) - 1)
   return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
   print(HANGMAN_PICS[len(missedLetters)])
   print()

   print('Ошибочные буквы ', end=' ')
   for letter in missedLetters:
      print(leter, end=' ')
   print()

   blanks = '_' * len(secretWord)

   for i in range(len(secretWord)):
      if secretWord[i] in correctLetters:
         blanks = blanks[:i] secretWord[i] + blanks[i+1:]
   
   for letter in blanks:
      print(letter, end=' ')
   print()

def getGuess(alreadyGuessed):
   while True:
      print('Введите букву ')
      guess = input('')
      guess = guess.lower()
      if len(guess) != 1:
         print('Введите одну букву!')
      elif guess in alreadyGuessed:
         print('Вы уже называли эту букву')
      elif not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
         print('Введите русскую букву ')
      else:
         return guess
