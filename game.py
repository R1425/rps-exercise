# this is the "game.py" file...

# IMPORT RANDOM : needed for computer choice section below
import random

# WELCOME MESSAGE
print("Welcome Player One! Lets play Rock, Paper, Scissors, Shoot!")

# USER INPUTS
humans_choice = input("Please make a selection ('rock' 'paper', 'scissors'):")
humans_choice = humans_choice.lower()

#You chose: 'rock'
print(f"You chose: '{humans_choice}' ")

# VALIDATE USER INPUTS 
valid_options = ["rock", "paper", "scissors"]

if humans_choice not in valid_options:
    print("Your selection is invalid. Rerun the game to try again!")
    exit()

#COMPUTER CHOICE    
computer_choice = random.choice(valid_options)
print("Computer chose:", computer_choice)

# DETERMINE THE WINNER 

#adapted from code shared in Slack by Bonnie:
# https://nyu-tech-2335.slack.com/archives/C5WPFSB52/p1657672686150239

if humans_choice == computer_choice:
    print("It's a tie!")
elif humans_choice == "rock":
    if computer_choice == "scissors":
        print("YOU WIN! Rock beats scissors!")
    else:
        print("You lose :( Paper beats rock. Better luck next time!")
elif humans_choice == "paper":
    if computer_choice == "rock":
        print("YOU WIN! Paper beats rock!")
    else:
        print("You lose :( Scissors beats paper. Better luck next time!")
elif humans_choice == "scissors":
    if computer_choice == "paper":
        print("YOU WIN! Scissors beats paper!")
    else:
        print("You lose :( Rock beats scissors. Better luck next time!")

#FAREWELL MESSAGE
print("Thanks for playing! See you next time")