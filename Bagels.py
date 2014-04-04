# My version of Chapter 11 of Al Sweigart's 'Invent Games With Python'
# bagels

import random

def getSecretNum(numDigits):
	'''Returns a string that is composed of unique random numbers
	that are numDigits long'''

	numbers = list(range(10))
	random.shuffle(numbers)
	secretNum = ''

	for i in range(numDigits):
		secretNum += str(numbers[i])
	return secretNum

def getClues(guess, secretNum):
	'''Returns clues to the user '''
	if guess == secretNum:
		return 'You got it!'

	clue = []

	for i in range(len(guess)):
		if guess[i] == secretNum[i]:
			clue.append('Fermi')
		elif guess[i] in secretNum:
			clue.append('Pico')

	if len(clue) == 0:
		return 'Bagels'

	clue.sort()
	return ' '.join(clue)

def isOnlyDigits(num):
	'''Returns True if num is a string composed only of integers '''

	if num == '':
		return False

	for i in num:
		if i not in '0 1 2 3 4 5 6 7 8 9'.split():
			return False

	return True

def playAgain():
	'''Does the player want to play again. Find out with this function '''

	return input('Do you want to play again? (yes or no) ').lower().startswith('y')

# Global Variables
NUMDIGITS = 3
MAXGUESS = 10

print('\nI am thining of a %d-digit number. Try to guess what it is.' % NUMDIGITS)
print('Here are some clues: ')
print('When I say:\tThat means:')
print('________________________________\n')
print('Pico\tOne digit is correct but in the wrong position.')
print('Fermi\tOne digit is correct and in the right position.')
print('Bagels\tNo digit is correct. None. Not one. Why is this game called bagels?')

while True:
	secretNum = getSecretNum(NUMDIGITS)
	print('I have thought up a number. You have %d guesses to get it' % MAXGUESS)

	numGuesses = 1
	while numGuesses <= MAXGUESS:
		guess = ''
		while len(guess) != NUMDIGITS or not isOnlyDigits:
			print('Guess #%d: ' % (numGuesses))
			guess = input()

		clue = getClues(guess, secretNum)
		print(clue)
		numGuesses += 1

		if guess == secretNum:
			break
		if numGuesses > MAXGUESS:
			print('You ran out of guesses. The answer was %s' % secretNum)

	if not playAgain():
		break
