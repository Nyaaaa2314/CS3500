import random

# This is the secret number
x = random.randint(0, 1000)

# This boolean indicates whether the user was successful or unsuccessful. It is initialized to False. Set this variable to True on victory.
status = False

print ("Hola! I am thinking of a number between 0 and 1000. You have 10 turns to guess it.")
numguess = 0

while numguess < 10:
	numguess = numguess + 1
	guess = int(input("What is your guess: "))
	if guess == x:
		print ("Congratulations! You found it.")
		status = True
		break
	elif guess < x:
		print ("Guess higher please.")
	else:
		print ("Guess lower please.")
	# TODO: Please write code that accepts a user guess, and displays the appropriate message.
	# Use the break statement to break out of the loop if the guess is correct. 
	# Set the status to True if the user correctly guessed the secret number. 

if status == False:
	print ("You lost the game. The secret number is " + str(x))


