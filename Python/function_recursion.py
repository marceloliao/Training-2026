"""
Recursion

Recursion is when a function calls itself.

Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.
"""


def coutdown(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        coutdown(n - 1)


coutdown(9)

""" 
Base Case and Recursive Case

Every recursive function must have two parts:

    A base case - A condition that stops the recursion
    A recursive case - The function calling itself with a modified argument

Without a base case, the function would call itself forever, causing a stack overflow error.

"""


def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)


print(factorial(8))

""" 
Fibonacci Sequence

The Fibonacci sequence is a classic example where each number is the sum of the two preceding ones. The sequence starts with 0 and 1:

0, 1, 1, 2, 3, 5, 8, 13, ...
"""


def fibonacci(n):
    # Base case
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(7))  # Output: 13

"""
Recursion with Lists    
"""


# Calculate the sum of all elements in a list
def sum_list(lst):
    sum = 0
    # Base case
    if len(lst) == 0:
        return 0
    # Recursive case
    else:
        sum = lst[0] + sum_list(lst[1:])
    return sum


print(sum_list([1, 3, 5, 7, 9]))  # Output: 25


# Find the maximum value in a list
def find_max(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        max_of_rest = find_max(numbers[1:])
        # return numbers[0] if numbers[0] > max_of_rest else max_of_rest
        return max(max_of_rest, numbers[0])


my_list = [3, 7, 2, 9, 1]
print(find_max(my_list))
