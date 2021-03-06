#################################
#####   Labyrinth 	    #####
#####	                    #####
##### Coded by Kyle Preston #####
#####	 2013	            #####	
################################# 
# This fucntion heavy game was inspired by the "Certain Death Riddle"
# from the film Labyrinth. There's also a nice brain
# teaser version posted on the Khan Academy

from time import *
from math import *
import sys

# Decorating functions
def dash():
	print ("-" * 80)

def star():
	print ("*" * 80)

def ques():
	print ("?" * 80)

# This function draws the doors
def doors():
	symbol = ['+', '*', '=', '^', '@', '.']
	for y in range(10):
		output = ""
		output2 = ""
		for x in range(15):
			numb = int((cos(x/4.0) * 3.0 + 2.0 + sin(y/4.0) * 3.0 + 2.0)/2.0)
			output += symbol[numb]
			output2 = (" " * 20) + output
		print output, output2

# Now begin the action and interaction functions
def intro():
	"""This is the introduction function. It walks the player through the game"""
	star(); dash(); dash()
	print ("\n\t\t\t|Labyrinth|\n")
	dash(); dash()
	sleep(3)

	print ("\nHere is the deal: You approach two doors with\ntwo creatures in front of them........\n")
	sleep(5.5)
	print ("Entering one of the doors will bring certain and\nsudden death to everything in the universe......\n")
	sleep(5.5)
	print ("Entering the other door will eliminate all evil\nin the universe. Leaving only that which is good and green -- forever.\n")
	star()
	go_on = raw_input("Are you with me so far? Enter yes, no or exit to run away crying: ")
	go_on = go_on.lower()
	if (go_on == 'yes' or go_on == 'y'):
		cont()
	elif (go_on == 'exit'):
		sys.exit(0)
	else:
		intro()
def cont():
	"""If the player is ready to continue"""
	star()
	print ("\nHere's what you know: the two creatures in front\nof you are simple-minded beasts.\n")
	sleep(5.5)
	print ("One of them can ONLY tell the truth and the other\none can ONLY lie but you do not know which one is which.\n ")
	sleep(6.5)
	print ("But they both know for certain what is behind each door.\n")
	sleep(5.5)
	go_on_on = raw_input("Are you still with me so far? Enter yes or no: ")
	go_on_on = go_on_on.lower()

	if (go_on_on == 'yes' or go_on_on == 'y'):
		question()
	else:
		cont()

def question():
	"""Prepares the player for the labyrinth riddle"""
	dash(); ques(); dash()
	print ("\nYou are allowed to ask one question and one\nquestion only.......\n")
	sleep(5)
	print ("Take some time and think about the question you will ask.")
	sleep(5)
	dash()
	ques()
	dash()
	print ("\n\nDoor # 1" + " " * 28 + "Door # 2\n")
	doors()
	print ("\n\n* hint * Draw a picture and really break it down.\nNothing to get stressed out about you know,\nit's only the fate of the universe at stake.\n")
	sleep(8)

# This function will break apart the users answer and determine
# if it is valid

def beast_one_question(input):
	"""Inputs the player's answer"""
	input = input.lower()
	usrlist = input.split()
	count = 0

	# for loop cycles through list version of users input.
	# A glitch in the game that needs fixing: users can 
	# just type these words in over and over again to get
	# a high enough key word total count but it won't matter
	# because they still won't know for sure what door to open
	# unless they solve the riddle.
	for i in range(0, len(usrlist)):

		if (usrlist[i] == 'beast2'):
			count += 1
		if (usrlist[i] == 'door' or usrlist[i] == 'door1' or usrlist[i] == 'door2'):
			count += 1
		if (usrlist[i] == 'choose' or usrlist[i] == 'select' or usrlist[i] == 'pick'):
			count += 1
		if (usrlist[i] == 'open'):
			count += 1
		if (usrlist[i] == 'would'):
			count += 1
		if (usrlist[i] == 'which'):
			count += 1
		if (usrlist[i] == 'what'):
			count += 1
		if (usrlist[i] == 'correct' or usrlist[i] == 'true' or usrlist[i] == 'right'):
			count += 1
		if (usrlist[i] == 'tell' or usrlist[i] == 'instruct' or usrlist[i] == 'advise' or usrlist[i] == 'suggest' or usrlist[i] == 'recommend' or usrlist[i] == 'say' or usrlist[i] == 'declare' or usrlist[i] == 'state'):
			count += 1

	return count

def beast_two_question(input):
	"""Inputs the player's answer"""
	input = input.lower()
	usrlist = input.split(' ')
	count = 0
	
	for i in range(0, len(usrlist)):

		if (usrlist[i] == 'beast1'):
			count += 1
		if (usrlist[i] == 'door' or usrlist[i] == 'door1' or usrlist[i] == 'door2'):
			count += 1
		if (usrlist[i] == 'choose' or usrlist[i] == 'select' or usrlist[i] == 'pick'):
			count += 1
		if (usrlist[i] == 'open'):
			count += 1
		if (usrlist[i] == 'would'):
			count += 1
		if (usrlist[i] == 'which'):
			count += 1
		if (usrlist[i] == 'what'):
			count += 1
		if (usrlist[i] == 'correct' or usrlist[i] == 'true' or usrlist[i] == 'right'):
			count += 1
		if (usrlist[i] == 'tell' or usrlist[i] == 'instruct' or usrlist[i] == 'advise' or usrlist[i] == 'suggest' or usrlist[i] == 'recommend' or usrlist[i] == 'say' or usrlist[i] == 'declare' or usrlist[i] == 'state'):
			count += 1

	return count

# Now comes the guessing part.
def guessing_game():
	"""Determines the answer given by the Beast"""
	beast = raw_input("You may refer to the creatures as Beast1 and\nBeast2 and the doors as door1 and\ndoor2. Which creature will you speak to?\n(Type Beast1 or Beast2): ").lower()

	if (beast == 'beast1'):
		guess = raw_input("What is your question to Beast1? (You do NOT need to type the ? at the end) ")
		print ("\n")
		total = beast_one_question(guess)
		
		if (total >= 5):
			print ("Beast1 tells you that Beast2 recommends door #2. \n")
			door_one()
		elif (total >= 3):
			print ("You're on the right track but should rephrase your question.\n")
			guessing_game()
		else:
			print ("Think harder. Lives are at stake!\n")
			guessing_game()
	elif (beast == 'beast2'):
		guess = raw_input("What is your question to Beast2? (You do NOT need to type the ? at the end) ")
		print ("\n")
		total = beast_two_question(guess)
		
		if (total >= 5):
			print ("Beast2 tells you that Beast1 recommends door #1.\n")
			door_two()
		elif (total >= 3):
			print ("You're on the right track but should rephrase your question.\n")
			guessing_game()
		else:
			print ("Think harder. Lives are at stake!\n")
			guessing_game()
	else:
		print ("\nThere is no %r\n " % beast)
		guessing_game()

# final stage
def door_one():
	"""Door 1 good. Door 2 bad. """
	print ("\nWill you follow its advice????\n")
	sleep(3)
	final_answer = raw_input("Which door will you open? Type 'Door1' or 'Door2': ").lower()
	print ("\n")
	if (final_answer == 'door1'):
		dash()
		print ("You walk through the door and immediately you feel it...........\n")
		dash()
		sleep(4)
		star(); dash()
		print ("The grey-rain curtain of this world turns all\nto silver glass and rolls back. You behold\nwhite shores and beyond them, a far green country under a swift sunrise\n\n")
		print ("\t\tThe universe is saved. Go get a sandwich and celebrate!\n")
		dash(); star()
		sys.exit(0)

	elif (final_answer == 'door2'):
		dash()
		print ("You walk through the door and immediately you feel it...........\n")
		dash()
		sleep(4)
		star(); dash()
		print ("Nothing. The nonexistence of everything -- the void.\nI'd tell you not to worry but it doesn't\nmatter because nothing exists.... \n\n")
		sleep(3)
		print ("n ")
		sleep(1)
		print ("o ")
		sleep(2) 
		print ("t ")
		sleep(3) 
		print ("h ") 
		sleep(4) 
		print ("i ") 
		sleep(5) 
		print ("........")
		dash(); star()
		sys.exit(0)
	else:
		print("Excuse me?\n")
		door_one()

def door_two():
	"""Door 2 good. Door 1 bad. """
	print ("\nWill you follow its advice????\n")
	sleep(3)
	final_answer = raw_input("Which door will you open? Type 'Door1' or 'Door2': ").lower()
	print ("\n")
	if (final_answer == 'door2'):
		dash()
		print ("You walk through the door and immediately you feel it...........\n")
		dash()
		sleep(4)
		star(); dash()
		print ("The grey-rain curtain of this world turns all\nto silver glass and rolls back. You behold\nwhite shores and beyond them, a far green country under a swift sunrise\n\n")
		print ("\t\tThe universe is saved. Go get a sandwich and celebrate!\n")
		dash(); star()
		sys.exit(0)

	elif (final_answer == 'door1'):
		dash()
		print ("You walk through the door and immediately you feel it...........\n")
		dash()
		sleep(4)
		star(); dash()
		print ("Nothing. The nonexistence of everything -- the void.\nI'd tell you not to worry but it doesn't\nmatter because nothing exists.... \n\n")
		sleep(3)
		print ("n ")
		sleep(1)
		print ("o ")
		sleep(2) 
		print ("t ")
		sleep(3) 
		print ("h ") 
		sleep(4) 
		print ("i ") 
		sleep(5) 
		print ("........")
		dash(); star()
		sys.exit(0)
	else:
		print("Excuse me?\n")
		door_one()

# Calling my intro function, which will cycle through my intro related functions
intro()
guessing_game()





