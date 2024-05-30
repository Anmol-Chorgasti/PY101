import random
import os

VALID_CHOICES = ['rock','paper','scissors']

def prompt(message):
    print(f'==> {message}')

def get_player_choice():
    prompt(f"Please choose one option from {', '.join(VALID_CHOICES)}")
    user_choice = input().lower()

    while user_choice not in VALID_CHOICES:
        prompt("Please enter a valid input")
        user_choice = input().lower()

    return user_choice

def get_computer_choice():
    computer_choice = random.choice(VALID_CHOICES)
    return computer_choice

def display_winner(player, computer):
    if ((player == 'rock' and computer == 'scissors') or
       (player == 'paper' and computer == 'rock') or
       (player == 'scissors' and computer == 'paper')):
        prompt("Player wins!")
    elif ((player == 'rock' and computer == 'paper') or
       (player == 'paper' and computer == 'scissors') or
       (player == 'scissors' and computer == 'rock')):
        prompt("Computer wins!")
    else:
        prompt("It's a tie!")


def play_again():
    continue_game = input().lower()

    while True:
        if continue_game.startswith('y') or continue_game.startswith('n'):
            break
        
        prompt("Please enter 'y' or 'n'")
        continue_game = input().lower()

    if (continue_game[0] == 'y'):
        return True
    
    return False


prompt("Welcome to the Rock Paper Scissors Game!")

while True:
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()

    prompt(f"You chose {player_choice}. Computer chose {computer_choice}")
    display_winner(player_choice, computer_choice)

    prompt("Would you like to play again? (y/n)")
    if not play_again():
        prompt("Thank you for playing the game!")
        break

    os.system('clear')