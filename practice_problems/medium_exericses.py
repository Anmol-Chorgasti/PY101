"""
For this practice problem, write a program that outputs The Flintstones Rock! 10 times, with each line prefixed by one more hyphen than the line above it. The output should start out like this:
"""
for number in range(1,11):
    print('-' * number, "The Flintstones Rock!", sep='')

"""
Alan wrote the following function, which was intended to return all of the factors of number:
Alyssa noticed that this code would fail when the input is a negative number, and asked Alan to change the loop. How can he make this work? Note that we're not looking to find the factors for negative numbers, but we want to handle it gracefully instead of going into an infinite loop.
"""
def factors(number):
    divisor = number
    result = []
    while divisor > 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result
print(factors(50))

"""

"""
print(False or 4)
