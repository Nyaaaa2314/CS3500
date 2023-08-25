import random
x = random.choice(["rock","paper","scissors"])
print("Lets play a game of Rock, Paper and Scissors")
user = input("I have selected mine, what do you select [type rock, paper or scissors]? ")
print("I chose ", x, ". You chose ", user,  ". ", end="")
if user == x:
    print("It's a tie.")
elif x == "rock" and user == "paper":
    print("You win.")
elif x == "paper" and user == "scissor":
    print("You win")
elif x == "scissors" and user == "rock":
    print("You win")
else:
    print("I win.")
