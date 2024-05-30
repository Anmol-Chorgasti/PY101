"""
A module to calculate the monthly mortgage payments user must make based on:
    1) Loan Amount
    2) Loan Duration in months
    3) Monthly Interest Rate

EDGE CASES
- The program considers <= 0% and > 100% interest rates as invalid rates,
- The duration of months should be such that loan_duration_months/12 should be an
integer
- Any loan amount below $1000 is considered too small and invalid
- Any loan above 10 million USD is considered too large and invalid
- If duration is less than 1 year or greater than 50 years, it is invalid

"""
# ----To-DO--------------
# X take user inputs for loan amount, duration, interest rate
# X verify inputs by checking them for format and edge case situations
# X test inputs by checking them for edge case situations
# X generate intermediate inputs such as duration in months, and monthly interest rate
# X calculate monthly payment
# X display monthly payment in $ and cents format
# X enable user to calculate multiple times
#------------------------

# helper function to display messages in a nicer format
def prompt(message):
    print(f'===> {message}')

def invalid_input(input_str): #checks if user input raises ValueError
    try:
        float(input_str)
    except ValueError:
        return True

    return False

# helper function to check if loan amount is valid and passes edge cases
def loan_check(loan_str):

    if not invalid_input(loan_str):
        loan_str = float(loan_str)

        if loan_str < 1000 or loan_str > 10_000_000:
            prompt("Loans can only be considered if they are\n"
                   'between 1000 USD and 10,000,000 USD')
            prompt("Please enter a valid loan amount:")
            return True
        return False

    #this code gets executed only if input cannot be coerced to float
    prompt("Hmmm, the input is invalid. Please try again:")
    return True

# helper function to check if duration period is valid and passes edge cases
def duration_check(duration_str):

    if not invalid_input(duration_str):
        duration_str = float(duration_str)

        if duration_str != round(duration_str,0):
            prompt("Please enter duration in an integer format: ")
            return True

        if duration_str < 1 or duration_str > 50:
            prompt("Please enter a period between 1 and 50 years (INCLUSIVE):")
            return True

        return False

    #this code gets executed only if input cannot be coerced to float
    prompt("Hmmm, the input is invalid. Please try again:")
    return True

# helper function to check if interest rate is valid and passes edge cases
def interest_check(interest_str):

    if not invalid_input(interest_str):
        interest_str = float(interest_str)

        if interest_str <= 0:
            prompt("Please enter a valid interest rate (example: 5,10,15):")
            return True

        if interest_str > 100:
            prompt("That is a really high interest rate.\n"
                   'We do not accept such high interest rates')
            prompt("Please enter a rate that is within our limits (1 to 100):")
            return True

        return False

    #this code gets executed only if input cannot be coerced to float
    prompt("Hmmm, the input is invalid. Please try again:")
    return True


# Welcome User
prompt("WELCOME to the mortgage calculator!\n")

# main logic of program
while True:
    # asking user to input loan amount
    prompt("Please enter the outstanding loan amount in numbers: ")
    loan = input()

    # verifying if loan amount passes all edge case tests
    while loan_check(loan):
        loan = input()

    # asking user to input loan duration
    prompt("Please enter the repayment duration for this loan (IN YEARS): ")
    duration_year = input()

    # verifying if duration passes all edge case tests
    while duration_check(duration_year):
        duration_year = input()

    # asking user to input interest percentage
    prompt("Please enter the annual interest rate for this loan: ")
    prompt("Hint: If it is 5%, please enter 5 and NOT 0.05 OR 5%")
    interest_year = input()

    # verifying if interest passes all edge case tests
    while interest_check(interest_year):
        interest_year = input()

    # generate the intermediate inputs required to calculate output
    loan = float(loan)
    duration_months = float(duration_year) * 12
    monthly_interest_rate = float(interest_year) / (100 * 12)

    # calculate output
    output =  loan * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-1 * duration_months)))
    output = round(output, 2) # to display amount in a format similar to $100.56
    total_repaid_amount = output * duration_months

    # displaying monthly mortage payment and predicted total amount repaid
    print()
    prompt(f"The monthly mortage payment is: ${output}\n")
    prompt(f"Your payments will total ${total_repaid_amount} after {duration_year} years")
    prompt(f"Your total interest will total ${round(total_repaid_amount - loan, 2)}\n")

    prompt("Would you like to calculate another mortgage payment?\n"
           "Please enter Y for yes\n"
           "Please enter N for no")
    choice = input()

    acceptable_choices = ['Y','y','n','N']
    while choice[0] not in acceptable_choices: # incase user enters yes or no
        print(choice[0])
        prompt("Please enter Y for yes\n"
                "Please enter N for no")
        choice = input()

    if choice not in acceptable_choices[0:2]:
        prompt("Thank you for using our mortgage calculator! :)")
        break