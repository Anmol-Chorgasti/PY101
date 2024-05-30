import random
import os

VALID_CHOICES = ['rock','paper','scissors','lizard','spock']
VALID_SHORTFORM_CHOICES = ['r','p','sc','l','sp']
MAX_POINTS = 3

def prompt(message):
    print(f'==> {message}')

# give user support on how to choose an option
def display_rules():
    prompt("Below are some rules for playing the game\n\n")
    print("Scissors cuts Paper covers Rock crushes\n"
           "Lizard poisons Spock smashes Scissors\n"
           "decapitates Lizard eats Paper disproves\n"
           "Spock vaporizes Rock crushes Scissors\n\n")
    prompt(f"The first player to reach {MAX_POINTS} points wins the game!\n\n")
    prompt(f"Please choose one option from {', '.join(VALID_CHOICES)}")

    for letter, word in zip(VALID_SHORTFORM_CHOICES, VALID_CHOICES):
        prompt(f"Enter {letter} or {word} to choose {word}")

    print()

# process user input if user enters shortform answer
def process_user_choice(choice):
    if len(choice) == 1:
        match choice:
            case 'r':
                return 'rock'
            case 'p':
                return 'paper'
            case 'l':
                return 'lizard'
    elif len(choice) == 2:
        match choice:
            case 'sc':
                return 'scissors'
            case 'sp':
                return 'spock'
    return choice

# take player choice as input and make sure it is valid
def get_player_choice():

    prompt("Please enter your choice: ")
    user_choice = input().lower()
    user_choice = process_user_choice(user_choice)

    while user_choice not in VALID_CHOICES:
        prompt("Please enter a valid input")
        user_choice = input().lower()
        user_choice = process_user_choice(user_choice)

    return user_choice

# generate computer choice
def get_computer_choice():
    computer_choice = random.choice(VALID_CHOICES)
    return computer_choice

# check if each choice below wins / loses / ties
def check_rock(computer):
    if computer in ('scissors','lizard'):
        return 'player'
    if computer in ('spock','paper'):
        return 'computer'
    return 'tie'

def check_paper(computer):
    if computer in ('rock','spock'):
        return 'player'
    if computer in ('lizard','scissors'):
        return 'computer'
    return 'tie'

def check_scissors(computer):
    if computer in ('paper','lizard'):
        return 'player'
    if computer in ('rock','spock'):
        return 'computer'
    return 'tie'

def check_lizard(computer):
    if computer in ('spock','paper'):
        return 'player'
    if computer in ('scissors','rock'):
        return 'computer'
    return 'tie'

def check_spock(computer):
    if computer in ('scissors','rock'):
        return 'player'
    if computer in ('lizard','paper'):
        return 'computer'
    return 'tie'

# determine result based on player and computer choices
def get_result(player, computer):
    match player:
        case 'rock':
            return check_rock(computer)
        case 'paper':
            return check_paper(computer)
        case 'scissors':
            return check_scissors(computer)
        case 'lizard':
            return check_lizard(computer)
        case 'spock':
            return check_spock(computer)

# display the result of each turn
def display_result(result):
    if result != 'tie':
        prompt(f"{result.capitalize()} wins this turn!\n")
    else:
        prompt(f"The choices are in! It is a {result}\n")

# display the current scores of the players involved after each turn
def display_current_score(player_count, computer_count):
    prompt(f"The current score:\n"
           f"Player: {player_count} , Computer: {computer_count}\n")

def display_grand_winner(winner):
    prompt(f"{winner} is the grand winner of this game!")
    print()

# main logic of the game
def run_game():
    player_count = 0
    computer_count = 0

    while player_count < MAX_POINTS and computer_count < MAX_POINTS:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()

        prompt(f"Player chose {player_choice}. Computer chose {computer_choice}")
        result = get_result(player_choice, computer_choice)

        if result == 'player':
            player_count += 1
        elif result == 'computer':
            computer_count += 1
        display_result(result)
        display_current_score(player_count, computer_count)

    if player_count == MAX_POINTS:
        display_grand_winner("Player")
    else:
        display_grand_winner("Computer")

def play_again():
    continue_game = input().lower()

    while True:
        if continue_game.startswith('y') or continue_game.startswith('n'):
            break

        prompt("Please enter 'y' or 'n'")
        continue_game = input().lower()

    if continue_game[0] == 'y':
        return True

    return False


# Program Start Point!!
prompt("Welcome to the Rock Paper Scissors Game!")

while True:
    display_rules()
    run_game()

    prompt("Would you like to play again? (y/n)")
    if not play_again():
        prompt("Thank you for playing the game!")
        break

    os.system('clear')