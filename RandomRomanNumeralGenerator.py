# This is a Random Roman Numeral Generator that tests the user's knowledge of Roman Numerals. I've found it to be a fantastic daily 
# brain food exercise!

# Kyle Preston
# 2014

import random

# Global Vars
correct = 0
total = 0
i = 0

def convertIntToRoman(random_number):
	"""Converts any number < 4000 to Roman Numerals. """

	roman_numerals = {
	1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
	10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
	100: 'C', 400: 'CD', 500: 'D', 900: 'CM',
	1000: 'M'
	}

	numeral = ''

	for key, value in sorted(roman_numerals.items(), reverse = True):
		while random_number >= key:
			numeral += value
			random_number -= key

	return numeral

print('_'* 55)
print('Convert the following Roman Numerals to our familiar\nDecimal Base-10 Number System\n')
print('\nPress CTRL-Z to escape')
print('_'* 55)

while i < 10:
	rando = random.randint(1, 3999)
	print(convertIntToRoman(rando))

	try:
		ans = int(raw_input("> "))
	except ValueError:
		ans = -1    # This passes a value that rando cannot be and hence fails the if statement

	if ans == rando:
		print('Correct!\n')
		correct += 1
		total += 1
	else:
		print('Nope. The answer was %d.\n' % rando)
		total += 1
	i += 1

print('Total correct: %d out of %d') % (correct, total)
