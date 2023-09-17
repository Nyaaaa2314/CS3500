import random
import sys

global n		# The number of sticks.
global aiNaiveData	# The AI data that helps in making choices for the naive AI.
aiNaiveData = list()
global aiTrainedData	# The AI data that helps in making choices for the trained AI.
aiTrainedData = list()
# aiData[i][j] (for either Naive or Trained data) where i is the number of remaining sticks,
# and j is the ball type (either 0, 1, 2 for ball types 1, 2, and 3 resp.)
global totalSticks	# Total number of sticks that can be chosen in a single turn.
totalSticks = 3

'''
Clear the screen. Usualy called to clear the screen and print the main menu.
'''
def clearScreen():
	print("\033[H\033[2J")
	sys.stdout.flush()

'''
Thus funciton prints the main menu, and accepts and returns a valid option.
'''
def printMenu(n):
	print ("Lets play a game of sticks.")
	print ("This is a 2 player game.")
	print ("There are " + str(n) + " sticks.")
	print ("In each turn a player can choose among 1 to 3 sticks.")
	print ("The player who chooses the last stick looses.")
	print ("\nGame Menu:")
	print ("1. Play against another human.")
	print ("2. Play against a naive A.I.")
	print ("3. Play against a trained A.I.")
	print ("4. Exit application.")
	
	option = int(input("What do you choose? [1-4]: "))
	while option < 1 or option > 4:
		print ("Please choose options [1-4]: ")
		option = int(input("What do you choose? [1-4]: "))
	
	return option;

'''
This funciton can be used to initialize all the aiData (either aiNaiveData or aiTrainedData) to all 1s.
Initially, all hats contain only one ball of each type. So aiData[i][j] = 1 means that when there are
i sticks on the board, the number of balls of type j (either 1, 2, or 3 balls, but note that this means
j is 0, 1 or 2) is 1.
'''
def initializeData(aiData):
	for i in range(n + 1):
		aiData.append([1, 1, 1])

'''
This function chooses a number of sticks as input from the human player. This takes as argument the number of remaining sticks. 
It prompts the user to enter either 1, 2 or 3 sticks and ensures that the human player doesn't choose more sticks than there are remaining. 
It also displays appropriate messages to the player. It always returns a valid choice that the player made.
'''
def humanChoose(remSticks):
	choose = int(input(""))
	while choose < 1 or choose > 3 or choose > remSticks:
		if choose > remSticks:
			print ("There are only \033[32m" + str(remSticks) + "\033[39;49m remaining. Please choose [1..3 or remaining sticks]: ", end = '')
		else:
			print ("You can only choose 1, 2 or 3 sticks. There are only \033[32m" + str(remSticks) + "\033[39;49m remaining. Please choose [1..3 or remaining sticks]: ", end = '')
		choose = int(input(""))
	return choose;

'''
This method simulates the two player human game.
'''
def playHuman():
	print ("\nHuman game")
	remSticks = n		# This is the number of remaining sticks.
	playerTurn = 0; # Whose turn is it? player 1 or 2 (corresponds to 0 or 1 resp.)

	# Simulate one human v human game. Call humanChoose to acquire a valid choice from the human player.
	# TODO:

	# You may use the following style to display to the user. 
	# print ("\033[34mplayer " + str(playerTurn + 1) + "\033[39;49m: There are \033[32m" + str(remSticks) + "\033[39;49m sticks remaining. How many do you choose [1..3 or remaining sticks]: ", end = '')

	winner = 1 # Set the winner in this variable, either 1 for player 1 or 2 for player 2. Change this variable to reflect the actual winner.
	print ("\n\033[33mPlayer " + str(winner) + " wins.\033[39;49m")	# Displays the final winner.

'''
This function takes in the number of remaining sticks and the ai data as arguments, and returns a choice made by the AI.
aiData can either be aiNaiveData or aiTrainedData. This funciton should look into this data, and make a valid choice.
Specifically, it should look at aiData[remSticks] -- which is an array of size 3 that contains the number of balls of each type.
Please write a function that returns either 1, 2 or 3 depending on its weight, i.e., based on the probability of the number of balls of each type.	
'''
def aiChoose(remSticks, aiData):
	# simulate an ai choice. Make sure that the choice is chosen based on the probability of the balls in hat remSticks.
	# TODO:
	return

'''
This function simulates the game - human vs ai. The aiOption indicates which AI to use. 0 is the Naive AI and 1 is the Trained AI.
aiData is set based on the aiOption. From here, both games (human vs Naive AI or human vs Trained AI) go through the same process (and hence no need to write two functions).
'''
def playAI(aiOption):
	# Initialize appropriate aiData
	aiData = list()

	if aiOption == 0:
		print("\nNaive AI")
		aiData = aiNaiveData
	else:
		print("\nTrained AI")
		aiData = aiTrainedData
	
	remSticks = n			# The number of sticks remaining.
	humanPlayer = 1		# The humman player
	aiPlayer = 2			# The AI player

	aiChoices = [0 for i in range(n + 1)] # The choices that the AI makes in one iteration or game.
	playerWon = humanPlayer	# Player that wins.

	# Simulate the game -- player vs AI.
	# TODO:
			
	# Update AI's choices.
	# TODO:

	# You may display the winner in the following format.
	# print ("\n\033[33mPlayer " + str(humanPlayer) + " wins.\033[39;49m")
	
'''
This function trains the AI for 100000 games.
'''
def trainingAI():

	numIterations = 100000	# Number of games or iterations.
	aiChoices = [[0 for i in range(n + 1)], [0 for i in range(n + 1)]]	# The choices that the AI makes. aiChoices[0] as the first player, and aiChoices[1] as the second player.
	remSticks = n		# Remaining number of sticks. Note that this needs to be set to n before the start of every iteration or game.
	playerWon = 0		# The player (or AI) who won.
	playerLost = 1	# The player (or AI) who lost.

	# Simulate numIterations number of games.
	for i in range(numIterations):

		# Initialize the ai choice for both players.
		aiChoices = [[0 for i in range(n + 1)], [0 for i in range(n + 1)]]
		# Initialize remaining number of sticks, and player won.
		remSticks = n
		playerWon = 0

		# Simulate one game. Keep track of the player that won, and the player that lost.
		# TODO:
					
		# Update the choices of both AI's and store them in aiTrainedData.
		# TODO:

if __name__ == "__main__":
	
	# Make sure the python program is called correctly with the right arguments.
	if len(sys.argv) != 2:
		print ("Wrong arguments. Please execute using")
		print ("$ python3 GameOfSticks.py <number of sticks>")
		print ("<number of sticks> should be in [10...100].")
		sys.exit(0)

	# Make sure that the number of sticks is valid (between 10 and 100).
	n = int(sys.argv[1])
	if n < 10 or n > 100:
			print ("Invalid <number of sticks>.")
			print ("You should have at least 10 and at most 100 sticks.")
			sys.exit(0)

	# First initialize all the data.
	initializeData(aiNaiveData)
	initializeData(aiTrainedData)
	trainingAI()
	
	# Application begins here.
	status = False
	while not status:
		clearScreen()
		option = printMenu(n)

		if option == 1:
			playHuman()
		elif option == 2:
			playAI(0)
		elif option == 3:
			playAI(1)
		else:
			status = True
		
		if option != 4:
			option = input("Press ENTER to get back to the menu.")
	
	print ("\nThanks for playing the game.")

