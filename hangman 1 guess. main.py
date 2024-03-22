import random
#ihangman pictures from sherry
HANGMAN_PICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
#group of words 
words = ("catalog","inventory","record","register","roll","file","index", "directory", "listing", "listicle",
         "checklist", "tally", "docket", "ticket","enumeration","table",'tabulation', 'nigga')
#function gives random wordds
def getRandomWord(words):
    return random.choice(words)
#i made use of len here to count 0-1
def displayBoard(missedLetters, correctLetters, Wordbank):
    print(HANGMAN_PICS[len(missedLetters)])
    print()
    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()
    print('The word is:', end=' ')
    for letter in Wordbank:
        if letter in correctLetters:
            print(letter, end=' ')
        else:
            print('_', end=' ')
    print()
#guess letter, it was kinda hard for me to give like a  clue i wanted to use sentences no time.
def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess
#function to play again as indicate
def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
Wordbank = getRandomWord(words)
gameIsDone = False
#this is a loop here for the rong or correct guesses
while True:
    displayBoard(missedLetters, correctLetters, Wordbank)
    guess = getGuess(missedLetters + correctLetters)
    if guess in Wordbank:
        correctLetters += guess
        if '_' not in correctLetters:
            print('Yes! The secret word is "' + Wordbank + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters += guess
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, Wordbank)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + Wordbank + '"')
            gameIsDone = True
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            Wordbank = getRandomWord(words)
            gameIsDone = False
        else:
            break

