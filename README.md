# Rock, Paper, Scissors, Shoot!

This is a fun game of rock, paper, scissors - human versus computer! 

## Prerequisites

This was created using 
+ Andaconda 4.12.0
+ Python 3.8

## Setup

The [rps-exercise repository](https://github.com/R1425/rps-exercise) can either be:
1. Forked (creating a copy of the repository) then cloned to create the remote repository on your local computer, or 
2. Cloned directly from the rps-exercise repository

***REMEMBER WHERE YOU CLONED THE REPOSITORY TO ON YOUR LOCAL COMPUTER***

Navigate to where you downloaded the respository using the command-line.  For the sake of this README file, we will assume we used the "Documents" folder:

```sh
cd ~/Documents/rps-exercise
```

Create a virtual environment (suggested naming is my-game-env but could be anything of your choice):

```sh
conda create -n my-game-env python=3.8
```

Activate the environment:

```sh
conda activate my-game-env
```

## Usage

### Option 1: Default the human player name

With this option, the human player's name will default to 'Player One'. Run the rock paper scissors game:

```sh
python game.py
```

### Option 2: Name the human player

With this option, you can name your player anything you would like. Run the rock paper scissors game: 

```sh
PLAYER_NAME="#enter desired name here" python game.py
```

### Below applies after either option 1 or option 2 above

You will recieve a welcome message then be prompted to make a selection from an available list as the human player.  Options include rock, paper, or scissors and will be displayed on your screen.  Enter your selection.  Assuming your selection is valid, the computer will then make their selection at random.  A message will display indicating if you won or lost and thank you for playing.  

If the human selection is invalid, you will be notified as such and the game will end.  To replay the game: 

```sh
python game.py
```

## DEMO

Here is a demo of Player One (human player) selecting 'paper' and the computer selecting 'rock'.  Player One wins and is thanked for playing.

    Welcome Player One! Lets play Rock, Paper, Scissors, Shoot!
    Please make a selection ('rock' 'paper', 'scissors'):paper
    You chose: 'paper'
    Computer chose: rock
    YOU WIN! Paper beats rock!
    Thanks for playing! See you next time