import random
import os
from time import sleep

VALID_CHOICES = ['rock','paper','scissors','lizard','spock']
VALID_SHORTFORM_CHOICES = {
    'r':'rock', 'p':'paper','sc':'scissors','l':'lizard','sp':'spock'
}
WINNING_COMBINATIONS = {
    'rock': ['scissors','lizard'],
    'paper': ['rock','spock'],
    'scissors': ['paper','lizard'],
    'lizard': ['paper','spock'],
    'spock': ['scissors', 'rock']
}
MAX_POINTS = 3
VALID_AFFIRMATIONS = ['y','yes','ye','yeah','yep','yea','ya','yokay','yo']
VALID_DENIALS = ['n','nope','nuh-uh','nein','nyet','nada','no way','not',
                 'no chance','negative','not right now','no mood','no']

def prompt(message):
    print(f'==> {message}')

def clear_screen(time):
    sleep(time)
    os.system('clear')

# give user support on how to choose an option
def display_rules():
    prompt("Below are some rules for playing the game\n\n")
    print("Scissors cuts Paper covers Rock crushes\n"
           "Lizard poisons Spock smashes Scissors\n"
           "decapitates Lizard eats Paper disproves\n"
           "Spock vaporizes Rock crushes Scissors\n\n")
    prompt(f"The first player to reach {MAX_POINTS} points wins the game!\n\n")
    prompt(f"Please choose one option from {', '.join(VALID_CHOICES)}")

    for key, value in VALID_SHORTFORM_CHOICES.items():
        prompt(f"Enter {key} or {value} to choose {value}")

    print()

# process user input if user enters shortform answer
def expand_user_choice(choice):
    if len(choice) == 1:
        match choice:
            case 'r':
                return VALID_SHORTFORM_CHOICES['r']
            case 'p':
                return VALID_SHORTFORM_CHOICES['p']
            case 'l':
                return VALID_SHORTFORM_CHOICES['l']
    elif len(choice) == 2:
        match choice:
            case 'sc':
                return VALID_SHORTFORM_CHOICES['sc']
            case 'sp':
                return VALID_SHORTFORM_CHOICES['sp']
    return choice

# take player choice as input and make sure it is valid
def get_player_choice():

    prompt("Please enter your choice: ")
    user_choice = input().lower().strip()
    user_choice = expand_user_choice(user_choice)

    while user_choice not in VALID_CHOICES:
        prompt("Please enter a valid input")
        user_choice = input().lower().strip()
        user_choice = expand_user_choice(user_choice)

    return user_choice

# generate computer choice
def get_computer_choice():
    computer_choice = random.choice(VALID_CHOICES)
    return computer_choice

# determine result based on player and computer choices
def get_result(player, computer):
    if computer in WINNING_COMBINATIONS[player]:
        return 'player'
    if player in WINNING_COMBINATIONS[computer]:
        return 'computer'
    return 'tie'

# display the result of each turn
def display_result(result, player_choice, computer_choice):

    prompt("PREVIOUS ROUND RESULTS!")
    prompt(f"Player chose {player_choice}. Computer chose {computer_choice}")
    if result != 'tie':
        prompt(f"{result.capitalize()} won the previous round!\n")
    else:
        prompt(f"The previous round was a {result}!\n")

# display the current scores of the players involved after each turn
def display_current_score(player_count, computer_count):
    prompt(f"The current score:\n"
           f"Player: {player_count} , Computer: {computer_count}\n")

def get_grand_winner(player):
    if player == MAX_POINTS:
        return 'Player'
    return 'Computer'

def display_grand_winner(winner):
    prompt(f"{winner} is the grand winner of this game!\n\n")

def always_display(player_count, computer_count):
    ui_line = '-' * 50
    print(f"{ui_line}\n")
    display_current_score(player_count, computer_count)
    print(ui_line)
    display_rules()

def increment_player_count(result, player_count):
    if result == 'player':
        return player_count + 1
    return player_count

def increment_computer_count(result, computer_count):
    if result == 'computer':
        return computer_count + 1
    return computer_count

# main logic of the game
def run_game():
    player_count = 0
    computer_count = 0

    while player_count < MAX_POINTS and computer_count < MAX_POINTS:
        always_display(player_count, computer_count)
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()

        result = get_result(player_choice, computer_choice)
        player_count = increment_player_count(result, player_count)
        computer_count = increment_computer_count(result, computer_count)

        clear_screen(0)
        display_result(result, player_choice, computer_choice)

    display_current_score(player_count, computer_count)
    display_grand_winner(get_grand_winner(player_count))


def yes_or_no(user_input):
    if len(user_input) == 1: #allowing for y and n inputs
        return user_input
    if user_input in VALID_AFFIRMATIONS:
        return user_input
    if user_input in VALID_DENIALS:
        return user_input
    return 'invalid'

def play_again():
    continue_game = input().lower()
    continue_game = yes_or_no(continue_game)

    while True:
        if continue_game.startswith('y') or continue_game.startswith('n'):
            break

        prompt("Please enter 'y' or 'n'")
        continue_game = input().lower()
        continue_game = yes_or_no(continue_game)

    if continue_game[0] == 'y':
        return True

    return False


# Program Start Point!!
prompt("Welcome to the Rock Paper Scissors Game!")

while True:
    run_game()

    prompt("Would you like to play again? (y/n)")
    if not play_again():
        prompt("Thank you for playing the game!")
        break

    clear_screen(0.5)


"""
old logic for determining winner

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
"""