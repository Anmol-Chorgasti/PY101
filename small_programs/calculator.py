# X Take two numbers as user input
# X Ask user for operation to perform on the two numbers
# X Perform operation specified by user on the two numbers
# X Display the final result back to the user
# X improve user interface
# X check if both numbers and operation entered are valid
# ask if user wants to calculate again?

import json

with open('calculator_messages.json', 'r') as file: #reading json in read mode
    data = json.load(file) #data is now a dictionary

def prompt(message):
    print(f"====> {message}")

def invalid_number(number_str): #number_str is entered in string format
    #using try except to catch error and return True or false
    try:
        int(number_str)
    except ValueError:
        return True
    return False

prompt(data["Welcome"])

RUN = True

while RUN:

    prompt(data["Input number 1"])
    number1 = input()

    #loop to prompt user to enter input until input is valid
    while invalid_number(number1):
        prompt(data["Invalid input"])
        number1 = input()

    prompt(data["Input number 2"])
    number2 = input()

    #loop to prompt user to enter input until input is valid
    while invalid_number(number2):
        prompt(data["Invalid input"])
        number2 = input()


    prompt(data["Input operation"])
    operation = input()

    #operation can only ever be in the list [1,2,3,4,5] to be valid
    while operation not in ['1','2','3','4','5']:
        prompt(data["Invalid operation"])
        operation = input()

    #using match case as that is more readable
    match operation:
        case '1':
            output = int(number1) + int(number2)
        case '2': #2 represents subtraction
            output = int(number1) - int(number2)
        case '3': #3 represents multiplication
            output = int(number1) * int(number2)
        case '4': #4 represents division
            output = int(number1) / int(number2)
        case '5': #5 represents exponentiation
            output = int(number1) ** int(number2)

    prompt(f"The result is: {output}")

    print()
    prompt(data["Calculate again"])
    choice = input()

    while choice not in ['y', 'Y', 'n', 'N']:
        prompt(data["Invalid calculate again"])
        choice = input()

    if choice in ['N','n']:
        RUN = False
    else:
        continue