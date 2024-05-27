# X Take two numbers as user input
# X Ask user for operation to perform on the two numbers
# X Perform operation specified by user on the two numbers
# X Display the final result back to the user

print("Welcome to Calculator!")

print("Please enter the first number: ")
number1 = input()

print("Please enter the second number: ")
number2 = input()

print('Please enter which operation you would like to perform\n'
      '1) Add 2) Subtract 3) Multiply 4) Divide 5) Exponent')
operation = input()


if operation == '1': #1 represents addition
    output = int(number1) + int(number2)
elif operation == '2': #2 represents subtraction
    output = int(number1) - int(number2)
elif operation == '3': #3 represents multiplication
    output = int(number1) * int(number2)
elif operation == '4': #4 represents division
    output = int(number1) / int(number2)
elif operation == '5': #5 represents exponentiation
    output = int(number1) ** int(number2)
else:
    output = -1
    print("Please enter a valid operation")

print(f"The result is: {output}")