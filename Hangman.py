import random

HangmanPics = ['''

  +-------------+
  |             |
                |
                |
                |
                |
                |
                |
                |
                |
=================''', '''

  +-------------+
  |             |
  O             |
                |
                |
                |
                |
                |
                |
                |
=================''', '''

  +-------------+
  |             |
  O             |
  |             |
                |
                |
                |
                |
                |
                |
=================''', '''

  +-------------+
  |             |
  O             |
 /|             |
                |
                |
                |
                |
                |
                |
=================''', '''

  +-------------+
  |             |
  O             |
 /|\            |
                |
                |
                |
                |
                |
                |
=================''', '''

  +-------------+
  |             |
  O             |
 /|\            |
 /              |
                |
                |
                |
                |
                |
=================''', '''

  +-------------+
  |             |
 0=             |
 /|\            |
 / |            |
                |
                |
                |
                |
                |
=================''']

def getWordList(txt_file):
	"""Reads and returns a list of words from file_name."""
	# using a list comprehension
	word_list = [word.lower() for line in open(txt_file, 'r') for word in line.split()]
	return word_list

def getRandomWord(txt_file):
	"""Returns a random string from the word_list."""

	word_list = getWordList(txt_file)
	# randint actually includes the highest value, so the -1 is necessary
	word_index = random.randint(0, len(word_list)-1)
	return word_list[word_index]

def displayBoard(HangmanPics, missed_letters, correct_letters, secret_word):
	"""Displays the most up-to-date game board """

	print(HangmanPics[len(missed_letters)])

	for letter in missed_letters:
		print letter,

	blanks = '_' * len(secret_word)

	# must replace blanks with correctly guessed letters
	for i in range(len(secret_word)):
		if secret_word[i] in correct_letters:
			blanks = blanks[:i] + secret_word[i] + blanks[i+1:]

	print('\n')

	# show the secret word with spaces in between 
	for letter in blanks:
		print(letter),

def goodGuess(user_input):
	"""Checks user input """
	
	if len(user_input) != 1:
		return False
	elif user_input in missed_letters or user_input in correct_letters:
		return False
	elif user_input not in 'abcdefghijklmnopqrstuvwxyz':
		return False
	return True

# Global Variables
secret_word = getRandomWord('words.txt')
playerWon = False
playerStillPlaying = True
missed_letters = []
correct_letters = []

print('_'*15)
print('H A N G M A N')
print('_'*15)
print('\n Enter a single LETTER from the alphabet')

while playerStillPlaying:
	displayBoard(HangmanPics, missed_letters, correct_letters, secret_word)
	guess = raw_input('Guess a letter: ').lower()
	
	if goodGuess(guess):
		
		if guess in secret_word:
			for i in range(secret_word.count(guess)):
				correct_letters.append(guess)
			if len(correct_letters) == len(secret_word):
				playerWon = True
				playerStillPlaying = False
		else:
			missed_letters.append(guess)
			if len(missed_letters) == 6:
				playerWon = False
				playerStillPlaying = False

if playerWon:
	displayBoard(HangmanPics, missed_letters, correct_letters, secret_word)
	print('\tYou won the game! YEEEEAAAHHHH!!!\n')

else:
	print (HangmanPics[6])
	print('\nYou lost. The word was "%s". Better luck next time!\n' % secret_word)
