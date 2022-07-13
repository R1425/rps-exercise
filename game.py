import random


print("Rock, Paper, Scissors, Shoot!")



# USER INPUTS


user_choice = input("Please make a selection ('rock' 'paper', 'scissors'):")

#You chose: 'rock'
print("You chose:", user_choice)
print(f"You chose: '{user_choice}' ")

# VALIDATE USER INPUTS 


#COMPUTER CHOICE    

#import random

valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)
print("Computer Choise:", computer_choice)