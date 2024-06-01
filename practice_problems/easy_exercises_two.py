"""
Question 1
Write two distinct ways of reversing the list without mutating the original list.
"""
numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]
reverse_numbers = numbers[::-1]
reverse_numbers1 = list(reversed(numbers))
print(numbers)
print(reverse_numbers)
print(reverse_numbers1)


"""
Question 2
Given a number and a list, determine whether the number is included in the list
"""
numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]
number1 = 8  # False (not in numbers)
number2 = 95 # True (in numbers)
print(number1 in numbers)
print(number2 in numbers)

"""
Question 3
Programmatically determine whether 42 lies between 10 and 100, inclusive. Do the same for the values 100 and 101,
"""
print(42 in list(range(10,101)))
print(100 in list(range(10,101)))
print(101 in list(range(10,101)))

"""
Question 4
Given a list of numbers [1, 2, 3, 4, 5], mutate the list by removing the number at index 2, so that the list becomes [1, 2, 4, 5].
"""
numbers = [1,2,3,4,5]
numbers.pop(2)
print(numbers)

"""
Question 5
How would you verify whether the data structures assigned to the variables numbers and table are of type list?
"""
numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}
print(isinstance(numbers, list))
print(isinstance(table, list))

"""
Question 6
Back in the stone age (before CSS), we used spaces to align things on the screen. If we have a 40-character wide table of Flintstone family members, how can we center the following title above the table with spaces?
"""
title = "Flintstone Family Members"
length = len(title)
number_of_spaces = (40 - length) / 2
print(" " * int(number_of_spaces-1), title)
print(title.center(40))

"""
Question 7
Write a one-liner to count the number of lower-case t characters in each of the following strings:
"""
statement1 = "The Flintstones Rock!"
statement2 = "Easy come, easy go."
print(sum([1 for element in statement1 if element == 't']))
print(sum([1 for element in statement2 if element == 't']))

"""
Question 8
Determine whether the following dictionary of people and their age contains an entry for 'Spot':
"""
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}
print('Spot' in ages.keys())

"""
Question 9
We have most of the Munster family in our ages dictionary:
"""
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}
additional_ages = {'Marilyn': 22, 'Spot': 237}
for key,value in additional_ages.items():
    ages[key] = value
print(ages)
#ages.update(additional_ages)