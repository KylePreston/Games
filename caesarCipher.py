# This Caesar Cipher script contains functions that will either encrypt
# or decrypt a message for you, as long as you know the key.

# For a visualization: http://inventwithpython.com/cipherwheel/
# import pyperclip
# import random

# Global Variables
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

numericalAlphabet = {

	'A': 0, 'B': 1, 'C': 2, 'D': 3,
	'E': 4, 'F': 5, 'G': 6, 'H': 7,
	'I': 8, 'J': 9, 'K': 10, 'L': 11,
	'M': 12, 'N': 13, 'O': 14, 'P': 15,
	'Q': 16, 'R': 17, 'S': 18, 'T':19,
	'U': 20, 'V': 21, 'W': 22, 'X': 23,
	'Y': 24, 'Z': 25
}

# Functions
def draw_box(n=30):
	print('_'*n)

def encryptionMode():
	'''Returns either Encryption or Decryption mode '''

	print('\n(Type E or D)')
	answer = raw_input('Would you like to encrypt a message of your own or decrypt a received message?\n').upper()
	if answer.startswith('E'):
		return 1
	else:
		return 0

def getDisplay():
	'''User display '''

	if encryptionMode():
		try:
			sentence = raw_input('\nType your message: ')
			code_key = int(raw_input('Choose a code key: (1 - 25) '))
			draw_box()
			print('Encryption: '),
			print(encryptMessage(sentence, code_key))
			draw_box()
		except ValueError:
			print('Need to type a number!')

	else:
		try:
			sentence = raw_input('\nType your message: ')
			code_key = int(raw_input('What is the code key? '))

			draw_box()
			print('Decryption: '),
			print(decryptMessage(sentence, code_key))
			draw_box()
		except ValueError:
			print('Need to type a number!')

def encryptMessage(message, code_key):
	'''Returns an encrypted version of the message '''

	message = list(message.upper())
	charNumber = 0
	for char in message:
		encryptionNumber = 0
		if char in abc:
			encryptionNumber = numericalAlphabet.get(char) + code_key
			if encryptionNumber >= 26:
				encryptionNumber -= 26
			
			for combo in sorted(numericalAlphabet.items()):
				if combo[1] == encryptionNumber:
					del(message[charNumber])
					message.insert(charNumber, combo[0])
					charNumber += 1
					break
		else:
			charNumber += 1

	return ''.join(message)

def decryptMessage(message, code_key):
	'''Returns a decrypted version of the message '''

	message = list(message.upper())
	charNumber = 0

	for char in message:
		decryptionNumber = 0
		if char in abc:
			decryptionNumber = numericalAlphabet.get(char) - code_key
			if decryptionNumber < 0:
				decryptionNumber += 26

			for combo in sorted(numericalAlphabet.items()):
				if combo[1] == decryptionNumber:
					del(message[charNumber])
					message.insert(charNumber, combo[0])
					charNumber += 1
					break
		else:
			charNumber += 1

	return ''.join(message)

# Main 
getDisplay()
