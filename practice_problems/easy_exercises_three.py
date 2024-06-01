"""
Question 1
Write two different ways to remove all of the elements from the following list:
"""
numbers = [1, 2, 3, 4]
numbers1 = numbers.copy()
numbers.clear()
while numbers1:
    numbers1.pop()
#numbers1 = numbers1[0:0] - this does not clear the elements from the original list
print(numbers, numbers1)

